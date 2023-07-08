from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)

    def __str__(self):
        return self.first_name


    def register(self):
        self.save()

    def isExists(self):
        # we do try and except bcs what if no customer exists in our database
        # in that case we don't have anything to match
        # so will give error
        # so if error just do except and return false, means no customer of
        # this email id exists yet
        try:
            Customer.objects.get(email=self.email)
            return True
        except Customer.DoesNotExist:
            return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
