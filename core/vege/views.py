from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# login kind of maintains the session and logout destroys the session

# Create your views here.
@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        image = request.FILES.get('image')
        description = data.get('description')

        Recipe.objects.create(
            name=name,
            image=image,
            description=description,
        )
        messages.success(request, "Recipe added successfully")

        return redirect('/recipes/')
    
    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        print(request.GET.get('search'))
        queryset = queryset.filter(name__icontains=request.GET.get('search'))
    context = {'page':'Recipes', 'recipes':queryset}
    
    return render(request,'recipes.html', context)

@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        image = request.FILES.get('image')
        description = data.get('description')

        queryset.name = name
        queryset.image = image
        queryset.description = description
        if image:
            queryset.image = image
        queryset.save()
        messages.success(request, "Recipe updated successfully")

        return redirect('/recipes/')
    
    context = {'page':'Update Recipe', 'recipe':queryset}
    return render(request,'update_recipe.html', context)



def delete_recipe(request, id):
    print(id)
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    messages.success(request, "Recipe deleted successfully")
    return redirect('/recipes/')


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
            return redirect('/recipes/')
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

