from rest_framework.test import APITestCase

from django.contrib.auth import get_user_model

from blogs.model import BlogPost

User = get_user_model()

class BlogPostAPITestCase(APITestCase):

    def set_up(self):

        user_obj = User(username="testrajan",email="testrajani@rajani.com")
        user_obj.set_password("thisiswar")
        user_obj.save()
        blog_post = BlogPost.objects.create(
            user=user_obj,
            title="Sexy Test",
            content="random test"
            )
        
        def test_single_user(self):
            user_count = User.objects.count()
            self.assertEqual(user_count,1)

