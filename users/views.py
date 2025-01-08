from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def signin(request):
    return render(request, 'users/signin.html')


def mypage(request):
    return render(request, 'users/mypage.html')




# def user_join(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         join_location_password = request.POST.get('join_location_password')
#         localid = request.POST.get('location_id')
        
#         print(f'join location password : {join_location_password}, localid : {localid}')
#         print(f'join location password type: {type(join_location_password)}, localid type: {type(localid)}')
#         try:
#             location = Localinfo.objects.get(localid=localid)
#             print(f'got it')
#         except Localinfo.DoesNotExist:
#             messages.error(request, 'fail!!')
#             return redirect('accounts:login')

#         if int(location.localid) != int(join_location_password):
#             messages.error(request, 'Invalid location password.')
#             return redirect('accounts:login')


#         if form.is_valid():
#             print(f'{localid} and {join_location_password}',2)
#             user = form.save(commit=False)
#             user.location = location  
#             user.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('accounts:login')
#         else:
#             print(f"Form is invalid: {form.errors}")

#     else:
#         form = CustomUserCreationForm()

#     locations = Localinfo.objects.all() 
#     return render(request, 'accounts/login.html', {'form': form, 'locations': locations})


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('main:main')
#         else:
#             messages.error(request, 'Invalid username or password')

    
#     locations = Localinfo.objects.values('localid', 'localalias')
#     context = {
#         'locations': locations  
#     }
#     return render(request, 'accounts/login.html', context)

# def user_logout(request):
#     logout(request)
#     return redirect('accounts:login') 

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