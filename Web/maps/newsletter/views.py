from django.shortcuts import render

# Create your views here.
from .models import User
from .forms import UserForm
def home(request):
	form=UserForm()
	context={'form':form}
	return render(request,'form.html',context)

def search(request):
	if request.method=='POST':

		form=UserForm(request.POST)
		if form.is_valid():
			if User.objects.filter(email=form.cleaned_data['email']).exists():
				return render(request,'emailalready.html',{})
			form.save()
			return render(request,'thanks.html',{})
	return render(request,'form.html',{
		'form':UserForm
		})