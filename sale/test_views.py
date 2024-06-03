from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post, CarMake, CarModel

class TestPostViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.car_make = CarMake.objects.create(name='Toyota')
        self.car_model = CarModel.objects.create(make=self.car_make, name='Corolla')
        self.post = Post(
            title="Test Post",
            slug="test-post",
            author=self.user,
            car_model=self.car_model,
            production_year=2022,
            price=15000.00,
            content="This is a test post content.",
            excerpt="Post excerpt",
            status=1
        )
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse('post_detail', args=['test-post']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Post", response.content)
        self.assertIn(b"This is a test post content.", response.content)
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        self.client.login(username="myUsername", password="myPassword")
        post_data = {'body': 'This is a test comment.'}
        response = self.client.post(reverse('post_detail', args=['test-post']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Comment submitted and awaiting approval',response.content)