from django.shortcuts import render
from . import fake_model


def home(request):
    return render(request, 'index.html')

def results(request):
    user_input_age = request.GET.get("age")
    prediction = fake_model.fake_age(int(user_input_age))
    return render(request, 'results.html', {'prediction': prediction})