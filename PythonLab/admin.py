from django.contrib import admin

# Register your models here.
from .forms import TrainCreateForm
from .forms import InvoiceCreateForm
#from .forms import UserGetForm
from .models import Train
from .models import Invoice
#from .models import CustomUser


class TrainAdmin(admin.ModelAdmin):
    list_display = ["name", "cityTo", "cityFrom", "date"]
    ordering = ["name"]
    form = TrainCreateForm


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ["user", "train", "cost", "paid"]
    ordering = ["cost"]
    form = InvoiceCreateForm

"""
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "full_name", "email", "is_staff", "is_active", "date_joined"]
    ordering = ["date_joined"]
    form = UserGetForm
"""

admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(Train, TrainAdmin)
#admin.site.register(CustomUser, UserAdmin)
