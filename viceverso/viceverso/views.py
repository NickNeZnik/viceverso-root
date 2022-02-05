from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['viceversa_text']
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html', {'user_text':user_text,'reversed_text':reversed_text})	