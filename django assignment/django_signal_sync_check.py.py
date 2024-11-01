import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Define a receiver function that simulates a time-consuming task
@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    print("Signal received, starting task...")
    time.sleep(5)  # Simulate a long-running task
    print("Task completed.")
# Simulate saving a User instance
user = User(username='testuser')
user.save()
print("User save completed.")