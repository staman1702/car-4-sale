from django.test import TestCase
from django.contrib.auth.models import User
from .forms import CommentForm, CommentAdminForm, PostForm, PostAdminForm
from .models import Post, Comment, CarMake, CarModel


class TestCommentForm(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.car_make = CarMake.objects.create(name='Toyota')
        self.car_model = CarModel.objects.create(make=self.car_make, name='Corolla')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            car_model=self.car_model,
            production_year=2022,
            price=15000.00,
            content='This is a test post content.',
            status=1
        )
        
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='This is a test comment',
            approved=False
        )

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid(), msg='Comment Form should be valid with correct data')

    def test_form_is_invalid_missing_body(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg='Comment Form should be invalid without body')

    def test_form_updates_instance(self):
        comment_form = CommentForm({'body': 'Updated comment'}, instance=self.comment)
        self.assertTrue(comment_form.is_valid(), msg='Comment Form should be valid with correct data')
        updated_comment = comment_form.save()
        self.assertEqual(updated_comment.body, 'Updated comment', msg='Comment body should be updated')
        self.assertFalse(updated_comment.approved, msg='Comment should be marked as waiting for approvall')

class TestCommentAdminForm(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='testuser', password='testpass')
        self.car_make = CarMake.objects.create(name='Toyota')
        self.car_model = CarModel.objects.create(make=self.car_make, name='Corolla')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            car_model=self.car_model,
            production_year=2022,
            price=15000.00,
            content='This is a test post content.',
            status=1
        )
        
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='This is a test comment',
            approved=False
        )

    def test_form_is_valid(self):
        comment_admin_form = CommentAdminForm({'body': 'This is a great post', 'approved': True})
        self.assertTrue(comment_admin_form.is_valid(), msg='Admin Comment Form should be valid with correct data')

    def test_form_is_invalid_missing_body(self):
        comment_admin_form = CommentAdminForm({'body': '', 'approved': True})
        self.assertFalse(comment_admin_form.is_valid(), msg='Admin Comment Form should be invalid without body')

    def test_form_updates_instance(self):
        comment_admin_form = CommentAdminForm({'body': 'Updated comment', 'approved': True}, instance=self.comment)
        self.assertTrue(comment_admin_form.is_valid(), msg='Admin Comment Form should be valid with correct data')
        updated_comment = comment_admin_form.save()
        self.assertEqual(updated_comment.body, 'Updated comment', msg='Comment body should be updated')
        self.assertTrue(updated_comment.approved, msg='Comment should be marked as approved')

    def test_form_with_valid_initial_data(self):
        comment_admin_form = CommentAdminForm(instance=self.comment)
        self.assertEqual(comment_admin_form.initial['body'], 'This is a test comment')
        self.assertFalse(comment_admin_form.initial['approved'])


class TestPostForm(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.car_make = CarMake.objects.create(name='Toyota')
        self.car_model = CarModel.objects.create(make=self.car_make, name='Corolla')

    def test_form_is_valid(self):
        form_data = {
            'title': 'Test Post',
            'car_model': self.car_model.id,
            'production_year': 2022,
            'price': 15000.00,
            'content': 'This is a test post content.',
            'excerpt': 'Post excerpt',
        }
        form = PostForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid(), msg='Post Form should be valid with correct data')

    def test_form_is_invalid_missing_title(self):
        form_data = {
            'car_model': self.car_model.id,
            'production_year': 2022,
            'price': 15000.00,
            'content': 'This is a test post content.',
            'excerpt': 'Post excerpt',
        }
        form = PostForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid(), msg='Post Form should be invalid without title')

    def test_form_is_invalid_missing_car_model(self):
        form_data = {
            'title': 'Test Post',
            'production_year': 2022,
            'price': 15000.00,
            'content': 'This is a test post content.',
            'excerpt': 'Post excerpt',
        }
        form = PostForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid(), msg='Post Form should be invalid without car model')

    def test_form_updates_instance(self):
        post = Post.objects.create(
            title='Original Post',
            slug='original-post',
            author=self.user,
            car_model=self.car_model,
            production_year=2022,
            price=15000.00,
            content='This is a test post content.',
            excerpt='Post excerpt',
            status=1
        )
        form_data = {
            'title': 'Updated Post',
            'car_model': self.car_model.id,
            'production_year': 2022,
            'price': 15000.00,
            'content': 'This is an updated test post content.',
            'excerpt': 'Updated post excerpt',
        }
        form = PostForm(data=form_data, instance=post, user=self.user)
        self.assertTrue(form.is_valid(), msg='Post Form should be valid with correct data')
        updated_post = form.save()
        self.assertEqual(updated_post.title, 'Updated Post', msg='Post title should be updated')
        self.assertEqual(updated_post.content, 'This is an updated test post content.', msg='Post content should be updated')
        self.assertEqual(updated_post.excerpt, 'Updated post excerpt', msg='Post excerpt should be updated')



class TestPostAdminForm(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username='admin', password='adminpass')
        self.car_make = CarMake.objects.create(name='Toyota')
        self.car_model = CarModel.objects.create(make=self.car_make, name='Corolla')

    def test_form_is_valid(self):
        form_data = {
            'title': 'Test Post',
            'car_model': self.car_model.id,
            'production_year': 2022,
            'price': 15000.00,
            'content': 'This is a test post content.',
            'excerpt': 'Post excerpt',
            'status': 1
        }
        form = PostAdminForm(data=form_data, user=self.user)
        self.assertTrue(form.is_valid(), msg='Admin Post Form should be valid with correct data')

    def test_form_is_invalid_missing_title(self):
        form_data = {
            'car_model': self.car_model.id,
            'production_year': 2022,
            'price': 15000.00,
            'content': 'This is a test post content.',
            'excerpt': 'Post excerpt',
            'status': 1
        }
        form = PostAdminForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid(), msg='Admin Post Form should be invalid without title')

    def test_form_is_invalid_missing_car_model(self):
        form_data = {
            'title': 'Test Post',
            'production_year': 2022,
            'price': 15000.00,
            'content': 'This is a test post content.',
            'excerpt': 'Post excerpt',
            'status': 1
        }
        form = PostAdminForm(data=form_data, user=self.user)
        self.assertFalse(form.is_valid(), msg='Admin Post Form should be invalid without car model')

    def test_form_updates_instance(self):
        post = Post.objects.create(
            title='Original Post',
            slug='original-post',
            author=self.user,
            car_model=self.car_model,
            production_year=2022,
            price=15000.00,
            content='This is a test post content.',
            excerpt='Post excerpt',
            status=1
        )
        form_data = {
            'title': 'Updated Post',
            'car_model': self.car_model.id,
            'production_year': 2022,
            'price': 15000.00,
            'content': 'This is an updated test post content.',
            'excerpt': 'Updated post excerpt',
            'status': 1
        }
        form = PostAdminForm(data=form_data, instance=post, user=self.user)
        self.assertTrue(form.is_valid(), msg='Admin Post Form should be valid with correct data')
        updated_post = form.save()
        self.assertEqual(updated_post.title, 'Updated Post', msg='Post title should be updated')
        self.assertEqual(updated_post.content, 'This is an updated test post content.', msg='Post content should be updated')
        self.assertEqual(updated_post.excerpt, 'Updated post excerpt', msg='Post excerpt should be updated')
