from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Define a receiver function that modifies the database
@receiver(post_save, sender=User)
def my_handler(sender, instance, **kwargs):
    instance.username = 'modifieduser'
    instance.save()
# Use a transaction block to demonstrate rollback
try:
    with transaction.atomic():
        user = User(username='testuser')
        user.save()
        raise Exception("Simulate an error to trigger rollback")
except Exception as e:
    print("Transaction rolled back due to error.")
# Check if the user was saved
if User.objects.filter(username='modifieduser').exists():
    print("User modification persisted.")
else:
    print("User modification rolled back.")