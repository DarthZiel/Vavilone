from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class IncomeCategory(models.Model):
    title = models.CharField(max_length=100)

class ExpensesCategory(models.Model):
    title = models.CharField(max_length=100)
class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    cost = models.IntegerField()
    date = models.DateField()
  

    def __str__(self):
        return f"Доход стоимосью {self.cost} от {self.date}, сделанный {self.user}"

class Expenses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(ExpensesCategory, on_delete=models.CASCADE)
    cost = models.IntegerField()
    date = models.DateField()


    def __str__(self):
        return f"Расходы стоимосью {self.cost} от {self.date}, сделанный {self.user}"

