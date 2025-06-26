from django.test import TestCase
from django.utils import timezone
from datetime import datetime
from todo.models import Task

# Create your tests here.
class SampleTestCase(TestCase):
    def test_sample(self):
        self.assertEqual(1 + 2, 3)
 
class TaskModelTestCase(TestCase):
    def test_create_task(self):
        due = timezone.make_aware(datetime(2024, 6, 30, 23, 59, 59))
        task = Task(title='task1', due_at=due)
        task.save()

        task = Task.objects.get(pk=task.pk)
        self.assertEqual(task.title, 'task1')
        self.assertFalse(task.completed)
        self.assertEqual(task.due_at, due)

    def test_create_task2(self):
        task = Task(title='task2')
        task.save()

        task = Task.objects.get(pk=task.pk)
        self.assertEqual(task.title, 'task2')
        self.assertFalse(task.completed)
        self.assertEqual(task.due_at, None)

    def test_is_overdue_future(self):
        due = timezone.make_aware (datetime(2024, 6, 30, 23, 59, 59))
        current = timezone.make_aware(datetime(2024, 6, 30, 0, 0, 0))
        task = Task(title='task1', due_at=due)
        task.save()
        self.assertFalse(task.is_overdue(current))

    def test_is_overdue_past():
        due = timezone.make_aware(datetime(2024, 6, 30, 23, 59, 59))
        check_time = timezone.make_aware(datetime(2024, 7, 10, 0, 0, 0))
        task = Task(title='overdue task', due_at=due)
        task.save()
        assert task.is_overdue(check_time) is True
    
    def test_is_overdue_none():
        check_time = timezone.make_aware(datetime(2024, 7, 10, 0, 0, 0))
        task = Task(title='no due')
        task.save()
        assert task.is_overdue(check_time) is False