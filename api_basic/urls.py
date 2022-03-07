from django.urls import path
from .views import (
    ArticleDetail,
    GenericAPIView,
    article_list,
    article_detail,
    ArticleAPIView,
)

urlpatterns = [
    # path('article/', article_list),
    # path("article/", ArticleAPIView.as_view()),
    # path('article/<int:pk>/', article_detail)
    # path("article/<int:id>/", ArticleDetail.as_view()),
    path("generic/article/<int:id>/", GenericAPIView.as_view()),
    path("generic/article/", GenericAPIView.as_view()),
]
