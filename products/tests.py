from django.test import TestCase

from .models import Product,User
# Create your tests here.
class ProductTest(TestCase):
    def setUp(self):
        owner = User.objects.create_user(
            username="user1",
            password="user12345",
            email="user@mail.com",
        )
        product = Product.objects.create(
            name="yams",
            quantity=20,
            price=0.12,
            owner=owner
        )

    def test_product_creation(self):
        owner = User.objects.get(username="user1")
        product = Product.objects.create(name="yams",quantity=20,price=0.12,owner=owner)
        self.assertTrue(Product.objects.filter(id=1,name="yams").exists()) 
    
    def test_decimal_validation(self):
        # try:
        product = Product.objects.get(name="yams")
        product.price = 120.21
        product.save()

        price = Product.objects.get(name="yams")
        price  = float(price.price)
        return self.assertEqual(120.21,price)
        # except:
        #     print("invalid decimal")