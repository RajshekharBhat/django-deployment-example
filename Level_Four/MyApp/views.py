from django.shortcuts import render

# Create your views here.
def mane_view(request):
    context_dict={'text':"hello world","number":100}
    return render(request,"MyApp/mane_html.html",context=context_dict)

def other_view(request):
    return render(request,"MyApp/other_html.html")


def relative_templates_view(request):
    return render(request,"MyApp/relative_templates_html.html")
