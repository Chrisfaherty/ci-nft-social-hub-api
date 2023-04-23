from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username="sam", password="password")

    def test_can_list_posts(self):
        sam = User.objects.get(username='sam')
        Post.objects.create(owner=sam, title="This is a title")
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='sam', password='password')
        response = self.client.post('/posts/', {'title': 'This is a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_logged_out_user_can_not_create_post(self):
        response = self.client.post('/posts/', {'title': 'This is a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        sam = User.objects.create_user(username='sam', password='password')
        mat = User.objects.create_user(username='mat', password='password')
        Post.objects.create(
            owner=sam, title='This is a title', content='sams content'
        )
        Post.objects.create(
            owner=mat, title='This is another title', content ='mats content'
        )
    
    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'],'This is a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_can_not_fetch_post_by_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_posts(self):
        self.client.login(username='sam', password='password')
        response = self.client.put('/posts/1/', {'title': 'This is a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'This is a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
