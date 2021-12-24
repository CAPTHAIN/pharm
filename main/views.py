from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import *
from .forms import *

import json


class MedicinePageView(ListView):
    model = Medicine
    template_name = 'main/medicine.html'
    context_object_name = 'medicines'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cities'] = City.objects.all()
        context['points'] = Point.objects.filter(city=self.kwargs['city_pk'])
        context['medicines'] = Medicine.objects.filter(pid=str(self.kwargs['point_pk']))
        context['city'] = City.objects.get(id=self.kwargs['city_pk']).name
        context['address'] = Point.objects.get(pid=str(self.kwargs['point_pk'])).address
        context['user_pid'] = int(self.request.user.username)
        context['my_medicine'] = []
        return context


class MainPageView(ListView):
    model = City
    template_name = 'main/main.html'
    context_object_name = 'cities'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PointsPageView(ListView):
    model = Point
    template_name = 'main/medicine.html'
    context_object_name = 'points'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        points = Point.objects.filter(city=self.kwargs['city_pk'])
        pid_list = []
        address_list = []
        for point in points:
            pid_list.append(point.pid)
            address_list.append(point.address)
        my_point = Point.objects.get(pid=int(self.request.user.username)).pid
        my_medicine = Medicine.objects.filter(pid=my_point)
        context['points'] = points
        context['cities'] = City.objects.all()
        context['medicines'] = Medicine.objects.filter(pid__in=pid_list)
        context['city'] = City.objects.get(id=self.kwargs['city_pk']).name
        context['address'] = address_list
        context['my_medicine'] = my_medicine
        context['user_pid'] = int(self.request.user.username)

        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
