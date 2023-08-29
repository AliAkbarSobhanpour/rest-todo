from django.test import TestCase
from .models import Todo
# Create your tests here.


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(
            title = "this is title",
            body = "this is body"
        )
    

    def test_model_content(self):
        self.assertEqual(self.todo.title, "this is title")
        self.assertEqual(self.todo.body, "this is body")
        self.assertEqual(str(self.todo), "this is title")