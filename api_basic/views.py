from django.shortcuts import render

# Create your views here.
from django .http import HttpResponse,JsonResponse
from rest_framework.parsers import  JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt

""" function based api views
@csrf_exempt #for doing post operation , for get operation we don't need it
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serilaizer = ArticleSerializer(data = data)

        if serilaizer.is_valid():
            serilaizer.save()
            return  JsonResponse(serilaizer.data, status=201)
        return  JsonResponse(serilaizer.errors, status= 400)



@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk = pk)
    except Article.DoesNotExist:
        return  HttpResponse(status=404)

    if request.method == 'GET':
        serialzer = ArticleSerializer(article)

        return  JsonResponse(serialzer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serialzer = ArticleSerializer(article, data = data)

        if serialzer.is_valid():
            serialzer.save()
            return  JsonResponse(serialzer.data)
        return  JsonResponse(serialzer.errors, status= 400)

    elif request.method == 'DELETE':
        article.delete()
        return  HttpResponse(status=204)
"""

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

"""@api_view(['GET','POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
"""


from rest_framework import generics,mixins
from rest_framework.authentication import SessionAuthentication,BasicAuthentication # for
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

"""
class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id = None):
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self,request , id = None):
        return  self.create(request)

    def put(self,request, id = None):
        return self.update(request, id)

    def delete(self,request, id =None):
        return self.destroy(request, id)

"""

# another method for GET,POST,PUT,DELETE
from rest_framework import viewsets

class ArticleViewset(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()