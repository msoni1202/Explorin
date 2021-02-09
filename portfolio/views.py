from django.shortcuts import render

def homepage(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')

def projects(request):
	return render(request,'projects.html')

def contacts(request):
	return render(request,'contacts.html')

def task1(request):
	return render(request,'task1.html')

def task2(request):
	return render(request,'task2.html')

def task3(request):
	return render(request,'task3.html')

def task4(request):
	return render(request,'task4.html')

def task5(request):
	return render(request,'task5.html')

def task6(request):
	return render(request,'task6.html')

def form(request):
	return render(request,'form.html')

def task7(request):
	return render(request,'task7.html')

def final(request):
	return render(request,'final.html')
