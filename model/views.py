from django.shortcuts import render
from model.form import StudentsForm
# Create your views here.

def index(request):
    stud=StudentsForm
    return render(request, 'index.html', {'form:stud'})