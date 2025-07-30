from kavenegar import *
from django.conf import settings

# کلید API خود را اینجا یا بهتر از آن در فایل settings.py قرار دهید
# settings.KAVENEGAR_API_KEY = 'Your-API-Key'

def send_sms(receptor, message):
    try:
        api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
        params = {
            'receptor': receptor,
            'message': message,
        }
        response = api.sms_send(params)
        print(f"SMS Sent: {response}")
    except APIException as e:
        print(f"SMS API Error: {e}")
    except HTTPException as e:
        print(f"SMS HTTP Error: {e}")