from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from .models import Users


class UserListView(ListView):
    model = Users
    template_name = 'users/user/user_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = Users
    template_name = 'users/user/user_detail.html'


class UserCreateView(CreateView):
    model = Users
    fields = ['name', 'surname', 'phone']
    template_name = 'users/user/users_form.html'


class UserUpdateView(UpdateView):
    model = Users
    fields = ['name', 'surname', 'phone']
    template_name = 'users/user/users_update.html'


class UserDeleteView(DeleteView):
    model = Users
    success_url = '/'
    template_name = 'users/user/user_delete.html'


class SearchResultsView(ListView):
    model = Users
    template_name = 'users/user/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Users.objects.filter(
            Q(name__icontains=query) | Q(surname__icontains=query) | Q(phone__icontains=query)
        )
        return object_list
