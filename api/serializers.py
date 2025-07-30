from rest_framework import serializers
from .models import TimeSlot

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = '__all__' # این به صورت خودکار فیلد جدید را شامل می‌شود

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        # فیلد جدید را به لیست اضافه کنید
        fields = ['user_name', 'user_phone', 'user_age', 'consultation_topic']
