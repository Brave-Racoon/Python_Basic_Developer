
from django.test import TestCase
from products.models import Products
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your tests here.

class ProductsTest(TestCase):
    fixtures = ['products.json']

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@test.com')
        self.user = User.objects.create_user(username='testuser2', password='testpassword', email='test2@test.com')
        self.users_list = list(User.objects.values_list('username', flat=True).order_by('id'))
        print('Added users: ', self.users_list)

    def test_login_required(self):
        self.user = User()
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

        # force login
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get('/')
        self.assertFalse(response.context['user'].is_anonymous)
        self.assertEqual(200, response.status_code)

    def test_products_qty(self):
        products_qty = len(Products.objects.all())
        self.assertEqual(products_qty, 30)

    def tearDown(self):
        self.client.logout()
        self.user = User.objects.filter(id=1).delete()
        self.user = User.objects.filter(id=2).delete()
        print('Logout. Users list:  ', list(User.objects.values_list('id', flat=True).order_by('id')))