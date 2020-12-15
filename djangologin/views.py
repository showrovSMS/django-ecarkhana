from django.shortcuts import render

# Create your views here.
def abc(request):

    return render(request,"front end/index.html",{'question_object':"",'option_objects': ""})

def abc2(request):

    return render(request,"front end/bike-index.html",{'question_object':"",'option_objects': ""})

def abc3(request):

    return render(request,"front end/bicycle-index.html",{'question_object':"",'option_objects': ""})
