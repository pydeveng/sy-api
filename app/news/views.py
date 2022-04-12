# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer


class ArticleApiView(APIView):

    def get(self, request, page=1, symbol='AAPL'):
        page_size = 10
        offset = (page - 1) * page_size
        print("From: {} to: {}".format(offset, (offset+page_size)))
        articles = Article.objects.filter(symbol=symbol).order_by('published')[offset:(offset+page_size)].all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


