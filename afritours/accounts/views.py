from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from tours.models import Category, Post
from tours.views import category_fun
from .forms import ContactForm
from .models import Contact
from datetime import date


# Create your views here.
def register (request):

    cats = Category.objects.all()

    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        email      = request.POST['email']
        password1  = request.POST['password1']
        password2  = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                 messages.info(request, 'Username taken')
                 return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists, Should you login?!')
                return redirect('register')

            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name,
				username=username, password=password1, email=email )
                user.save();
                return redirect('/')
                
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    else:
        return render(request, 'accounts/register.html', {
			"cats": cats,
			})

def login (request):
  
    cats = category_fun()
    

  
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Invalid credentials')
    else:
        return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html', {
		    "cats": cats,
		    })

def logout (request):
    auth.logout(request)
    return redirect('/')


def aboutus(request):

	cats = category_fun()

	return render(request, "accounts/aboutus.html", {
			"cats": cats,
			})

def contant(request):

	recent = Post.objects.all()[:5]
	cats = category_fun()

	if request.method == "POST":	
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data["name"]
			email = form.cleaned_data["email"]
			feedback = form.cleaned_data["feedback"]
			message = form.cleaned_data["message"]
			date = form.cleaned_data["date"]
			
			try:
				contact = Contact.objects.create(name=name, email=email,
						feedback=feedback, message=message, date=date)
				contact.save();
				messages.success(request, "Your message was send successfully. Thank you!")
				return redirect("contant");
			except Exception as e:
				messages.info(request, "Sending message failed. Please try again")
				return redirect("contant")

	else:
		form = ContactForm()

	return render(request, "accounts/contant.html", {
			"form": form,
			"cats": cats,
			"recent": recent,
			})








