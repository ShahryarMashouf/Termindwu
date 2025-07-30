from rest_framework import generics, status
from rest_framework.response import Response
from .models import TimeSlot
from .serializers import TimeSlotSerializer, BookingSerializer
# برای ارسال پیامک در آینده از این بخش استفاده می‌شود
from .sms_service import send_sms

class TimeSlotListView(generics.ListAPIView):
    """ لیستی از تمام زمان‌ها را نمایش می‌دهد """
    queryset = TimeSlot.objects.all().order_by('start_time')
    serializer_class = TimeSlotSerializer

class BookTimeSlotView(generics.UpdateAPIView):
    """ یک زمان مشخص را رزرو می‌کند """
    queryset = TimeSlot.objects.all()
    serializer_class = BookingSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_booked:
            return Response({"error": "این زمان قبلا رزرو شده است."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save(is_booked=True)

        # --- شروع بخش اصلاح شده ---
        # خطا به این دلیل است که strftime نمی‌تواند کلمه فارسی "ساعت" را پردازش کند.
        # پس ما ابتدا زمان را بدون کلمات فارسی فرمت می‌کنیم و سپس پیام نهایی را می‌سازیم.

        user_name = serializer.validated_data.get('user_name')
        user_phone = serializer.validated_data.get('user_phone')
        
        # ۱. زمان را با استفاده از کاراکترهای انگلیسی فرمت کنید
        time_for_message = instance.start_time.strftime('%Y-%m-%d %H:%M')

        # ۲. حالا پیام فارسی را با استفاده از متغیر بالا بسازید
        message = f"آقای/خانم {user_name} گرامی، وقت مشاوره شما در تاریخ {time_for_message} با موفقیت رزرو شد."
        
        # در اینجا می‌توانید پیامک را ارسال کنید
        # send_sms(user_phone, message)
        
        # --- پایان بخش اصلاح شده ---

        return Response(TimeSlotSerializer(instance).data)
