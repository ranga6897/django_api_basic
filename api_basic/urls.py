# from django.urls import path, include #
# # from .views import article_list , article_detail
# # from . views import article_list
# from .views import GenericAPIView
#
# urlpatterns = {
#     # path('article/', article_list),
#     # path('detail/<int:pk>/', article_detail),
#     path('generic/article/', GenericAPIView.as_view()),  # for viewing all at once
#     path('generic/article/<int:id>/', GenericAPIView.as_view()),  # for put and delete options
#     path('viewset/article/', ArticleViewset.as_view()),
# }


##  using viewset

from django.urls import path, include
from .views import ArticleViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')

urlpatterns = [

    path('viewset/', include(router.urls)),

]