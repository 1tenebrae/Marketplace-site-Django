from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.decorators import login_required
from shop.models import *


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,
                        'account/register_done.html',
                        {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})

@login_required
def profile(request):
    try:
        shop = Shop.objects.get(proprietor=request.user)
    except Shop.DoesNotExist:
        shop = None
    return render(request, 'account/profile.html', {'shop': shop})


def main(request):
    return render(request, 'account/main_page.html')
