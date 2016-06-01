from .models import Tasks
from django.test import TestCase
import datetime


class DisplayTasksTestCase(TestCase):
    def test_displays_tasks(self):
        Tasks.objects.create(title='Shopping', description='apple, eggs, milk', date='2016-06-11')
        Tasks.objects.create(title='Math exam', date='2016-07-18')
        response = self.client.get('/')
        self.assertContains(response, 'Shopping')
        self.assertContains(response, 'apple, eggs, milk')
        self.assertContains(response, '11 June 2016')
        self.assertContains(response, 'Math exam')
        self.assertContains(response, '18 July 2016')

    def test_all_tasks_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')


class TasksViewTestCase(TestCase):
    def test_add_task(self):
        response = self.client.post(
            '/add/',
            data={'title': 'Shopping', 'description': 'apple, eggs, milk', 'date': '2016-06-11'}
        )
        self.assertEqual(Tasks.objects.count(), 1)
        task = Tasks.objects.first()
        self.assertEqual(task.title, 'Shopping')
        self.assertEqual(task.description, 'apple, eggs, milk')
        self.assertEqual(task.date, datetime.date(2016, 6, 11))
        self.assertRedirects(response, '/')

    def test_fail_add_task(self):
        response = self.client.post(
            '/add/',
            data={'title': '', 'description': 'apple, eggs, milk', 'date': '12 January 2016'}
        )
        self.assertEqual(Tasks.objects.count(), 0)
        self.assertContains(response, 'invalid date format')
        self.assertContains(response, 'This field is required')

    def test_edit_task(self):
        Tasks.objects.create(title='Shopping', description='apple, eggs, milk', date='2016-06-11')
        task = Tasks.objects.first()
        response = self.client.get('/edit/%s' % task.id)
        response = self.client.post(
            response['Location'],
            data={'title': 'Math exam', 'description': '', 'date': '2016-08-12'}
        )
        updated_task = Tasks.objects.first()
        self.assertEqual(updated_task.title, 'Math exam')
        self.assertEqual(updated_task.description, '')
        self.assertEqual(updated_task.date, datetime.date(2016, 8, 12))
        self.assertRedirects(response, '/')

    def test_fail_edit_task(self):
        Tasks.objects.create(title='Shopping', description='apple, eggs, milk', date='2016-06-11')
        task = Tasks.objects.first()
        response = self.client.get('/edit/%s' % task.id)
        response = self.client.post(
            response['Location'],
            data={'title': '', 'description': '', 'date': '12 January 2016'}
        )
        self.assertContains(response, 'invalid date format')
        self.assertContains(response, 'This field is required')

    def test_delete_task(self):
        self.client.post(
            '/add/',
            data={'title': 'Shopping', 'description': 'apple, eggs, milk', 'date': '2016-06-11'}
        )
        task = Tasks.objects.first()
        self.assertEqual(Tasks.objects.count(), 1)
        response = self.client.get('/delete/%s/' % task.id)
        self.assertEqual(Tasks.objects.count(), 0)
        self.assertRedirects(response, '/')

    def test_tasks_templates(self):
        response = self.client.get('/add/')
        self.assertTemplateUsed(response, 'add_edit.html')
        Tasks.objects.create(title='Shopping', description='apple, eggs, milk', date='2016-06-11')
        task = Tasks.objects.first()
        response = self.client.get('/edit/%s/' % task.id)
        self.assertTemplateUsed(response, 'add_edit.html')


class TasksModelTestCase(TestCase):
    def test_tasks_model(self):
        Tasks.objects.create(title='Shopping', description='apple, eggs, milk', date='2016-06-11')
        self.assertEqual(Tasks.objects.count(), 1)
        Tasks.objects.update(title='Math exam', description='', date='2016-08-12')
        task = Tasks.objects.first()
        self.assertEqual(task.title, 'Math exam')
        self.assertEqual(task.description, '')
        self.assertEqual(task.date, datetime.date(2016, 8, 12))
        task.delete()
        self.assertEqual(Tasks.objects.count(), 0)
