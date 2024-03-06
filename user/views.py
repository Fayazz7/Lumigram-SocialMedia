from django.shortcuts import render, redirect
from django.views.generic import View, CreateView, TemplateView, UpdateView
from user.forms import *
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
# Create your views here.


class UserAuthView(View):
    def get(self, request, *args, **kwargs):
        signup_form = RegistrationForm()
        signin_form = LogInForm()
        return render(request, "signup.html", {"signup_form": signup_form, "signin_form": signin_form})

    def post(self, request, *args, **kwargs):
        signup_form = RegistrationForm(request.POST)
        signin_form = LogInForm(request.POST)

        if 'signup' in request.POST:
            if signup_form.is_valid():
                print(signup_form.cleaned_data)
                signup_form.save()
                return render(request, "signup.html")
            else:
                return render(request, "signup.html", {"signup_form": signup_form})
        elif 'signin' in request.POST:
            if signin_form.is_valid():
                print(signin_form.cleaned_data)
                user = authenticate(request, username=signin_form.cleaned_data.get(
                    "username"), password=signin_form.cleaned_data.get("password"))
                if user:
                    login(request, user)
                    print("success")
                    return redirect('home')
                else:
                    print("Failed")
                    return render(request, "signup.html", {"signin_form": signin_form})
            else:
                return render(request, "signup.html", {"signin_form": signin_form})


class SignOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('authentication')


class IndexView(View):
    def get(self, request, *args, **kwargs):
        qs = Post.objects.all().order_by('-created_at')
        return render(request, "index.html", {"post": qs})


class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm()
        return render(request, "add-post.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
            return render(request, "add-post.html", {"form": form})
        else:
            return render(request, "add-post.html", {"form": form})


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = UserProfile.objects.get(user=id)
        p_obj = Post.objects.filter(user=id)
        return render(request, "profile.html", {"user": qs, "post": p_obj})


class ProfileUpdateView(View):
    def get(self, request, *args, **kwargs):
        profile = request.user.profile
        form = UserProfileForm(instance=profile)
        return render(request, "profile-edit.html", {"form": form})

    def post(self, request, *args, **kwargs):
        profile = request.user.profile
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-view', pk=request.user.id)
        else:
            return render(request, "profile-edit.html", {"form": form})


class FollowUnFollowView(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        u_obj = User.objects.get(id=id)
        u_p_obj = u_obj.profile
        action = request.POST.get("connect")
        if action == "follow":
            request.user.profile.following.add(u_obj)
            u_p_obj.followers.add(request.user)
        elif action == "unfollow":
            request.user.profile.following.remove(u_obj)
            u_p_obj.followers.remove(request.user)
        return redirect('home')


class LikeUnLikeView(View):
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        postobj = Post.objects.get(id=id)
        user = request.user
