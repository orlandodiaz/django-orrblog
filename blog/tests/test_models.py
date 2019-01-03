from django.test import TestCase
from blog.models import Post
from django.utils import timezone
from django.contrib.auth.models import User


class UerModelTest(TestCase):
    """ Test the User model """


class PostModelTest(TestCase):
    """ Test the Post model"""

    @classmethod
    def setUpTestData(self):
        self.test_user1 = User.objects.create_user(
            username='testuser1', password='12345')
        self.test_user1.save()

    def create_post_model(self,
                          title="only a test",
                          body="test body",
                          body2="test body 2",
                          author=None):
        return Post.objects.create(
            title=title,
            body=body,
            body2=body2,
            author=self.test_user1,
            date_posted=timezone.now())

    def test_post_model_creation(self):
        post_object = self.create_post_model()
        self.assertTrue(isinstance(post_object, Post))
        self.assertEqual(post_object.__str__(), post_object.title)
