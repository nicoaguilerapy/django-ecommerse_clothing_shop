from django.db import models
from accounts.models import Profile
from cart.models import Order

class Wallet(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

    def get_money(self):
        transactions = Transaction.objects.filter(owner = self.owner)
        money = 0

        for t in transactions:
            money = t.mount + money
        
        return money

class Transaction(models.Model):
    id = models.AutoField(primary_key = True)
    owner = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    concept = models.CharField(max_length = 100, blank = False, null = False)
    code_transaction = models.IntegerField(default = 0, null=False, blank = False)
    date_transaction = models.DateTimeField(auto_now=True)
    code_annulment = models.IntegerField(default = 0, null=True, blank = True)
    date_annulment = models.DateTimeField(auto_now=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank = True)
    mount = models.IntegerField(null=False, blank = False)
    

    
