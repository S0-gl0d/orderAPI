import os
import django
from django.utils import timezone
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'orderAPI.settings')
django.setup()

from orderApp.models import OrderModel

OrderModel.objects.filter(created_at__lte=timezone.now() - timedelta(minutes=1)).delete()