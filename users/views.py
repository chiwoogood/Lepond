from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, AddressForm
from django.urls import reverse

def signin(request):

    return render(request, 'users/signin.html')

@login_required
def mypage(request):
    return render(request, 'users/mypage.html')


def user_signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # POST 요청에서 'next' 값을 가져옵니다.
            next_url = request.POST.get('next', reverse('main:main'))  # 기본 URL로 대체
            if not next_url.strip():  # next 값이 빈 문자열인 경우 처리
                next_url = reverse('main:main')
            messages.success(request, '로그인이 완료되었습니다.')
            return redirect(next_url)
        else:
            messages.error(request, 'Login failed. Please check your credentials.')
    
    return render(request, 'users/signin.html')

def user_signup(request):
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        address_form = AddressForm(request.POST)
        if user_form.is_valid() and address_form.is_valid():
            user = user_form.save()
            address = address_form.save(commit=False)
            address.user = user
            address.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('users:signin')
        else:
            messages.error(request, "Registration failed. Please correct the errors.")
    else:
        user_form = CustomUserCreationForm()
        address_form = AddressForm()

    context = {
        'user_form': user_form,
        'address_form': address_form,
    }
    return render(request, 'users/signin.html', context)

def user_signout(request):
    logout(request)
    messages.success(request, "로그아웃이 완료되었습니다.")
    return redirect('main:main') 

@login_required
def myorder(request):

    return render(request, 'users/myorder.html')

@login_required
def profile(request):
    
    return render(request, 'users/profile.html')

@login_required
def update(request):
    return render(request, 'users/update.html')

def user_update(request):
    pass
    
@login_required
def address(request):
    return render(request,'users/address.html')


def user_address_add(request):
    pass

def user_address_delete(request):
    pass

@login_required
def mycommunity(request):
    
    return render(request,'users/mycommunity.html')


# @login_required
# def user_update(request):
#     if request.method == 'POST':
#         form = CustomUserUpdateForm(request.POST, instance=request.user)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile was updated successfully!')
#             return redirect('main:main') 
#     else:
#         form = CustomUserUpdateForm(instance=request.user)
    
#     return render(request, 'accounts/update.html', {'form': form})

# @login_required
# def user_delete(request):
#     if request.method == 'POST':
#         user = User.objects.get(id=request.user.id)
#         user.delete()
#         return redirect('main:main')  
#     return render(request, 'accounts/delete.html')