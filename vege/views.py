from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# login kind of maintains the session and logout destroys the session

# Create your views here.
@login_required(login_url='/login/')
def opportunities(request):
    
    queryset = Opportunity.objects.all()
    # for opportunity in queryset:
    #         opportunity.description = ' '.join(opportunity.description.split()[:10])


    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(name__icontains=request.GET.get('search'))
    context = {'page':'Opportunities', 'opportunities':queryset}
    
    return render(request,'recipes.html', context)


def add_opportunity(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        image = request.FILES.get('image')
        description = data.get('description')
        role = data.get('role')
        op_link = data.get('op_link')
        status = data.get('status')
        batch = data.get('batch')
        location = data.get('location')

        user = request.user

        Opportunity.objects.create(
            user=user,
            name=name,
            image=image,
            description=description,
            role=role,
            op_link=op_link,
            status=status,
            batch=batch,
            location=location
        )
        messages.success(request, "Opportunity added successfully")
        return redirect('/opportunities/')
    context = {'page':'Add Opportunity'}
    return render(request,'add_recipe.html', context)


@login_required(login_url='/login/')
def update_opportunity(request, id):
    queryset = Opportunity.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        image = request.FILES.get('image')
        description = data.get('description')
        role = data.get('role')
        op_link = data.get('op_link')
        status = data.get('status')
        batch = data.get('batch')
        location = data.get('location')
        # status is a boolein field
        status = data.get('status')



        print("hhello")
        print(status)


        queryset.name = name
        queryset.image = image
        queryset.description = description
        queryset.role = role
        queryset.op_link = op_link
        queryset.status = status
        queryset.batch = batch
        queryset.location = location

        print(queryset.op_link)


        if image:
            queryset.image = image
        queryset.save()
        messages.success(request, "Opportunity updated successfully")

        return redirect('/opportunities/')
    
    context = {'page':'Update Opportunity', 'opportunity':queryset}
    return render(request,'update_recipe.html', context)


def delete_opportunity(request, id):
    print(id)
    queryset = Opportunity.objects.get(id=id)
    queryset.delete()
    messages.success(request, "Opportunity deleted successfully")
    return redirect('/opportunities/')


def login_page(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        if not User.objects.filter(username=username).exists():
           messages.error(request, "Invalid username or password")
           return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('/opportunities/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/login/')

    return render(request,'login.html', {'page':'Login'})

def logout_page(request):
    logout(request)
    messages.success(request, "Logout successful")
    return redirect('/login/')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username= request.POST.get('username')
        password= request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already exists")
            return redirect('/register/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username
        )

        # encrypt password
        user.set_password(password)
        user.save()
        messages.success(request, "User created successfully")
        return redirect('/register/')

    return render(request,'register.html', {'page':'Register'})

