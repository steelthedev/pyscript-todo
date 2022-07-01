from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.
@api_view(["GET"])
def GetTodo(request):
    if request.method == "GET":
        try:
            todo = Todo.objects.all()
        except:
            return HttpResponse(status = 404)
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)
