from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import *


class TestUrls(SimpleTestCase):
    def test_user_list(self):
        url = reverse('users:user_list')
        self.assertEquals(resolve(url).func.view_class, UserListView)

    def test_user_detail(self):
        url = reverse('users:user_detail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, UserDetailView)

    def test_user_create(self):
        url = reverse('users:user_create')
        self.assertEquals(resolve(url).func.view_class, UserCreateView)

    def test_user_update(self):
        url = reverse('users:user_update', args=['1'])
        self.assertEquals(resolve(url).func.view_class, UserUpdateView)

    def test_user_delete(self):
        url = reverse('users:user_delete', args=['1'])
        self.assertEquals(resolve(url).func.view_class, UserDeleteView)

    def test_user_search(self):
        url = reverse('users:search_results')
        self.assertEquals(resolve(url).func.view_class, SearchResultsView)



