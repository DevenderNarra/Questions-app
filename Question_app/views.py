from django.shortcuts import render

from django.http import JsonResponse,HttpResponse
from .serializers import QuestionSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import JsonResponse



from .models import Question

def home(request):
    return HttpResponse("Hello, Wel come to Questions Page.")


def get_all_questions(request):
    if request.method == 'GET':
        questions=Question.objects.all()
        serializer=QuestionSerializer(questions,many=True)
        return JsonResponse({'questions':serializer.data},safe=False)
    else:
        return JsonResponse({"Method is not a GET"})

def get_question(request,question_id):
    serializer=QuestionSerializer(Question.objects.get(id=question_id))
    return JsonResponse({'question':serializer.data},safe=False)

def create_question(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def update_question(request,question_id):
    if request.method == "POST":
        serializer = QuestionSerializer(data=request.data, instance=Question.objects.get(id=question_id))
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED,safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({"Method is not a POST"})


def delete_question(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        question.delete()
        return JsonResponse({"message": "Question deleted successfully"})
    except Question.DoesNotExist:
        return JsonResponse({"error": f"Question with id {question_id} does not exist"}, status=404)

