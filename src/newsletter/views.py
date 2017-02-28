from django.shortcuts import render

# Create your views here.
def home(request):
	title = "My Title %s" %(request.user)
	context = {
	   "template_title":abc,
	}
	return render(request, "home.html",context)
