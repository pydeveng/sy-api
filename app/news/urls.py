from django.urls import path, include

from .views import ArticleApiView

urlpatterns = [
    path("<str:symbol>/<int:page>/", ArticleApiView.as_view(), name="articles"),
]
