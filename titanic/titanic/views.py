from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def results(request):
    user_input_age = request.GET.get("age")
    return render(request, 'results.html', {'age': user_input_age})