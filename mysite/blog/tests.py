from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(
            title='first task',
            task='make test on GitHub CI',
        )

    def test_title_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.title}'
        self.assertEquals(expected_object_name, 'first task')

    def test_description_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.task}'
        self.assertEquals(expected_object_name, 'make test on GitHub CI')
