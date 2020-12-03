from django.shortcuts import render

# Create your views here.
def abc(request):

    return render(request,"index.html",{'question_object':"",'option_objects': ""})
