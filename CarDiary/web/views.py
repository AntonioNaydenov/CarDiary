from django.shortcuts import render, redirect

from CarDiary.web.forms import CreateProfileForm


def show_index(request):
    user = False
    if request.user.is_authenticated:
        user = True
    context = {
        'user_logged': user
    }
    return render(request, "home-page.html", context)


def register_page(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }

    return render(request, 'register-page.html', context)


def login_page(request):
    return render(request, 'login-page.html')
