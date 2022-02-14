from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def index(request):
	return HttpResponse("Less go!!!")

@api_view(['GET','POST'])
def article_list(request):
	if request.method == 'GET':
		articles = Article.objects.all() #getting all the article objects and saving them into articles var.
		serializer = ArticleSerializer(articles, many=True) #serializing the objects using the Arcileserializer class we created on serializer.py
		return Response(serializer.data) #returning the serialized objects as JSON.
	elif request.method == 'POST':
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return JsonResponse(serializer.errors, status = 400)

@api_view(['GET','PUT','DELETE'])
def article_details(request, pk):
	try:
		article = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		return Response("The article you are looking for doesnt exit.",status=404)

	if request.method == 'GET':
		serializer = ArticleSerializer(article)
		return Response(serializer.data)
	elif request.method == 'PUT':
		#updating the article with the new data sent from the client
		serializer = ArticleSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = 201)
		return Response(serializer.errors, status=400)
	elif request.method == 'DELETE':
		article.delete()
		return Response(status=204)
