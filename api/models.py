from django.db import models

class TimeSlot(models.Model):
    start_time = models.DateTimeField(unique=True)
    is_booked = models.BooleanField(default=False)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_phone = models.CharField(max_length=15, blank=True, null=True)
    user_age = models.IntegerField(blank=True, null=True)
    # فیلد جدید برای موضوع مشاوره
    consultation_topic = models.TextField(blank=True, null=True) # <-- این خط را اضافه کنید

    def __str__(self):
        return f"{self.start_time.strftime('%Y-%m-%d %H:%M')} - {'Booked' if self.is_booked else 'Available'}"