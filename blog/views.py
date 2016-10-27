from django.shortcuts import render
#this is regarding views
def post_list(request):
	return render(request,'blog/post_list.html',{})
