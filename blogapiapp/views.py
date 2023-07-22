from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def articleList(request):
    if request.method=='GET':
        articles =Article.objects.all()
        serializer =ArticleSerializer(articles,many=True)
        return Response(serializer.data)

    elif request.method=='POST':
        serializer=ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 


@api_view(['GET','PUT','DELETE'])
def article_details(request, slug):
    try:
        article = Article.objects.get(slug=slug)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer =ArticleSerializer(article)
        return Response(serializer.data)    
    
    elif request.method == "PUT":
        serializer = ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        article.delete()
        print("post deleted")
        return Response(status=status.HTTP_204_NO_CONTENT)
        


