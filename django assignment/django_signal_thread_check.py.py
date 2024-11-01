import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Define a receiver function that prints the current thread
@receiver(post_save, sender=User)
def my_handler(sender, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")
# Simulate saving a User instance
print(f"Main thread: {threading.current_thread().name}")
user = User(username='testuser')
user.save()