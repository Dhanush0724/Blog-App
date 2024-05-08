from django.shortcuts import render , redirect ,HttpResponse
from django.db.models import Q
from .models import PostModel ,savecon
from .forms import PostModelForm,UserUpdateForm,ProfileUpdateForm ,PostUpdateForm,CommentForm,SearchForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            return HttpResponse("User does not eixts: please register")
            
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('blog-index')
        else :
            return HttpResponse('username or password not amtch')
    context ={'page':page}
    return render(request, 'login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('blog-index')

def registerPage(request):
     
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =  form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('blog-index')
        else :
            return HttpResponse("eroor caused while register try once more")
    return render(request,'login_register.html', {'form':form})




#restric the content login_url will route the links
#@login_required will block the view page onlt login members can see this
@login_required(login_url='login')
def index(request):

    posts = PostModel.objects.all()
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
        return redirect('blog-index')
    else :
        
         form = PostModelForm()
        

    context = {
        'posts':  posts,
        'form' : form
    }
    return render(request,'blog/index.html' , context)

@login_required(login_url='login')
def indexprofile(request):
    posts = PostModel.objects.all()
    
    if request.method == 'POST':
            form = PostModelForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
                return redirect('blog-index')
    else :
                form = PostModelForm()
        
    

    
    context = {
        'posts':  posts,
        'form' : form
    }
    return render(request,'templates\profile.html' , context)
    
@login_required(login_url='login')
def profilePage(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None,instance=request.user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else :
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }

    # Render the profile page template with the user data
    return render(request, 'profile.html', context)


#CRUD operations on posts ||
@login_required(login_url='login')
def post_detail(request, pk):
    msg = False
    if request.user.is_authenticated:
        user = request.user
        post = PostModel.objects.get(id=pk)
        if post.likes.filter(id=user.id).exists():
            msg=True

    
    post = PostModel.objects.get(id=pk) #this pk grabs all the content in the posts detials and we can acces through this
    if request.method == 'POST':

        if request.user.is_authenticated:
            user = request.user
            if post.likes.filter(id=user.id).exists():
                post.likes.remove(user)
                msg= False
            else :
                post.likes.add(user)
                msg = True


        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instance =  c_form.save(commit=False)
            instance.user = request.user
            instance.post = post
            instance.save()
            return redirect('blog-post-details', pk=post.id)
    else :
        post = PostModel.objects.get(id=pk)
        c_form = CommentForm()
    context = {
        'post' : post,
        'c_form':c_form,
        'msg':msg
    }
    return render(request,'blog/post_details.html',context)


@login_required(login_url='login')
def post_edit(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-details' , pk=post.id)
    else :
        form = PostUpdateForm(instance=post)
    context = {
        'post':post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)
@login_required(login_url='login')
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post':post

    }
    return render(request, 'blog/post_delete.html')


@login_required(login_url='login')
def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        # Adjusted query to correctly reference the author's name
        results = PostModel.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(author__username__icontains=query)
        )
    else:
        results = PostModel.objects.none()

    return render(request, 'search.html', {'form': form, 'results': results})

def out(request):
    return render(request,'out.html')


def contact(request):
    return render(request,'contact.html')

def savecontact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Check if name is provided
        if name:
            # Create and save instance of savecon model
            en = savecon(name=name, email=email, message=message)
            en.save()
            return render(request, 'contact.html')  # Render success page after saving
        else:
            # Handle case where name is not provided
            return render(request, 'error.html', {'message': 'Name is required'})

    return render(request, 'contact.html')


