import datetime
import pytz

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase

from base.models import ToDo

User = get_user_model()
central = pytz.timezone('US/Central')


class ToDoApiTests(APITestCase):

    def setUp(self):
        self.john = User.objects.create(
            username='johndoe',
            email='john.doe@example.com')

        self.jane = User.objects.create(
            username='janedoe',
            email='jane.doe@example.com')

        ToDo.objects.create(
            title='Do stuff',
            user=self.john,
            completed_on=central.localize(
                datetime.datetime(2015, 8, 1, 12, 0, 0)))

        ToDo.objects.create(
            title='Do more stuff',
            user=self.john)

        ToDo.objects.create(
            title='Do yet more stuff',
            user=self.jane,
            completed_on=central.localize(
                datetime.datetime(2015, 8, 2, 12, 0, 0)))


    def test_get_users(self):
        '''Test that we can get a list of users.'''
        url = reverse('user-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['username'], 'johndoe')


    def test_get_todos(self):
        '''Test that we can get a list of todo items.'''

        url = reverse('todo-list')
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['title'], 'Do stuff')


    def test_filter_user_todos(self):
        '''Test that we can filter todos by user and completion.'''

        url = reverse('todo-list')

        # John (id == 1)
        response = self.client.get(url+'?user=1', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)


        # John's completed todos
        response = self.client.get(url+'?user=1&is_completed=true',
            format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Do stuff')


        # All completed todos
        response = self.client.get(url+'?is_completed=true', format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[1]['title'], 'Do yet more stuff')


    def test_create_user(self):
        '''Test that we can create a new user.'''

        url = reverse('user-list')

        response = self.client.post(
            url,
            {'username': 'jsmith', 'email': 'john.smith@example.com'},
            format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 3)

        self.assertEqual(User.objects.get(pk=3).username, 'jsmith')


    def test_create_todo(self):
        '''Test that we can create a new todo item.'''

        url = reverse('todo-list')

        response = self.client.post(
            url,
            {'title': 'Posted todo', 'user': 1},
            format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['id'], 4)

        self.assertEqual(ToDo.objects.get(pk=4).title, 'Posted todo')


    def test_complete_todo(self):
        '''Test that we can mark an incomplete todo item as completed.'''

        some_datetime = central.localize(
                datetime.datetime(2015, 8, 2, 12, 0, 0))

        self.assertEqual(ToDo.objects.get(pk=2).completed_on, None)

        url = reverse('todo-detail', kwargs={'pk': 2})

        data = {
            'title': 'Do more stuff',
            'user': 1,
            'completed_on': some_datetime.isoformat()
        }

        response = self.client.put(
            url,
            data,
            format='json')
        self.assertEqual(response.status_code, 200)

        self.assertEqual(ToDo.objects.get(pk=2).completed_on, some_datetime)
