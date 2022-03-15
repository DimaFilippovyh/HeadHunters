from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm


def register(request):
    """ Regsiter a new user if GET request made """
    if request.method != 'POST':
        # present user a registration form with no data
        form = UserCreationForm()
        profile_form = ProfileForm()
    else:
        # process a completed form with POST data
        form = UserCreationForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)

        if form.is_valid() and profile_form.is_valid():
            new_profile_form = profile_form.save(commit=False)
            new_user = form.save()
            new_profile_form.user = new_user
            new_profile_form.save()
            # Log in user and the redirect to home page

            login(request, new_user)
            return redirect('head_hunters:index')

    # Display blank or invalid form
    context = {'form': form, 'profile_form': profile_form}
    return render(request, 'registration/register.html', context)
