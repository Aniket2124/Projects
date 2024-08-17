from django.test import TestCase, Client
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.
class BlogTesting(TestCase):
    def setUp(self):
        # Create a test client
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com')
        self.post = Post.objects.create(title='Test Post', content='This is a test post.',user=self.user)

    def test_post_creation(self):
        # Check that the post title is correct
        self.assertEqual(self.post.title, 'Test Post')

        # Check that the post content is correct
        self.assertEqual(self.post.content, 'This is a test post.')

        # Check that the post is associated with the correct user
        self.assertEqual(self.post.user.username, 'testuser')

        # Verify that the post is saved in the database
        self.assertEqual(Post.objects.count(), 1)

        # Check that the post's string representation is as expected (if you have defined __str__)
        self.assertEqual(str(self.post), 'Test Post')

        # Check if the post is associated with the correct email
        self.assertEqual(self.post.user.email, 'testuser@example.com')

    
