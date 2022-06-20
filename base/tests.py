from django.test import TestCase
from base.models import User, Post, NeighbourHood, Business
from base.views import neighbour


class TestModel(TestCase):
   def test_create_user(self):
    user = User.objects.create_user(username='testuser', email='testuser@gmail.com', password1='testpassword', password2='testpassword')
    user.save()
    
    self.assertEqual(str(user), 'banana')
    
   def test_create_neighbourHood(self):
    user = User.objects.create_user(username='banana', email='banana@gmail.com', password1='password', password2='password')
    user.save()
    neighbourHood = NeighbourHood.objects.create(user=user.username, name='kiaguthu', location='Muranga, Kenya')
    neighbourHood.save()
    
    self.assertEqual(str(neighbourHood), 'kiaguthu')
    
   def test_create_post(self):
    user = User.objects.create_user(username='banana', email='banana@gmail.com', password1='password', password2='password')
    user.save()
    neighbourHood = NeighbourHood.objects.create(user=user.username, name='kiaguthu', location='Muranga, Kenya')
    neighbourHood.save()
    post = Post.objects.create(user=user, neighbourHood=neighbourHood, caption='just saying hi', )
    post.save()
    
    self.assertEqual(str(post), 'just saying hi')
    
   def test_create_bussiness(self):
    user = User.objects.create_user(username='banana', email='banana@gmail.com', password1='password', password2='password')
    user.save()
    neighbourHood = NeighbourHood.objects.create(user=user.username, name='kiaguthu', location='Muranga, Kenya')
    neighbourHood.save()
    
    bussiness = Business.objects.create(user=user, neighbour=neighbour, body='come all',image='image/upload/v1654464303/dhagnnfxtfd9ldneefvv.jpg',)
    bussiness.save()
    self.assertEqual(str(bussiness), 'come all')