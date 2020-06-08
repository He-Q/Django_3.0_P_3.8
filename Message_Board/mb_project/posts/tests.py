from django.test import TestCase
from django.urls import reverse


from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self):
        post = Post.objects.get(id = 1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a test')


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(
            text= "this is another test"
            )
    
    def test_view_url_exists_at_proper_location(self):
        responce = self.client.get('/')
        self.assertEqual(responce.status_code,200)


    def test_view_url_by_name(self):
        responce = self.client.get(reverse('home'))
        self.assertEqual(responce.status_code,200)


    def test_view_uses_correct_templates(self):
        responce = self.client.get(reverse('home'))
        self.assertEqual(responce.status_code,200)
        self.assertTemplateUsed(responce,'home.html')
    
