from django.test import TestCase
from .models import Todo
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase 
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

    def test_api_listview(self):
        response = self.client.get(reverse("todo-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)
    
    def test_api_detailview(self):
        response = self.client.get(
            reverse("todo-details", kwargs={"pk":self.todo.id}),
            format = "json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "this is title")
        