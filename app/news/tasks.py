import datetime
import celery
import json
from django.template.defaultfilters import slugify
from datetime import datetime
from time import mktime
import feedparser
from .models import Symbol, Article
from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule

YAHOO_URI = '''https://feeds.finance.yahoo.com/rss/2.0/headline?s={symbol}&region=US&lang=en-US'''


@periodic_task(run_every=(crontab(minute='*/1')), name="fetch_symbols", ignore_result=False)
def fetch_symbols():
    symbols = Symbol.objects.all()
    PeriodicTask.objects.all().delete()

    # Do Fetch from Yahoo
    for s in symbols:
        schedule = IntervalSchedule.objects.create(every=10, period=IntervalSchedule.SECONDS)
        task = PeriodicTask.objects.create(interval=schedule, name='''{0}-fetch'''.format(s.name),
                                           task='news.tasks.fetch_symbol_news',
                                           args=json.dumps([s.name]))
        task.save()
        print('''Spawning signal for symbol `{symbol_name}`.'''.format(
            symbol_name=s.name))


@celery.task()
def fetch_symbol_news(name):
    print("Symbol received")
    data = feedparser.parse(YAHOO_URI.format(symbol=name))

    for article in data["entries"]:

        article_data = Article(title=article["title"], link=article["link"], symbol=name)
        date = article.get("published_parsed", None)
        if date is None:
            date1 = datetime.datetime.now()
        else:
            date1 = datetime.fromtimestamp(mktime(date))
        article_data.published = date1
        article_data.description = article.get("summary", None)
        article_data.guid = article.get("guid")
        try:
            art = Article.objects.get(slug=slugify(article["title"]))
        except Article.DoesNotExist:
            print(article_data.title)
            article_data.save()
            continue

        article_data.id = art.id
        article_data.save(force_update=True)
