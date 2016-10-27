from django.shortcuts import render
#this is comment
def post_list(request):
	return render(request,'blog/post_list.html',{})
