# Django otp provider

* OTP
* Transport: SMS or EMAIL
* Async (celery)
* Custom SMS providers


### Requirements
+ Python >= 3.0
+ Django >= 2.0
+ Celery
+ PyJWT

### Schema
1. Install `django-otp-provider` library
2. Create your custom  class extends from `BaseTransport` and implement `send_code`
3. In settings.py add:
`
OTP_PROVIDER = {
    'TRANSPORT_TYPE': "SMS",
    'TRANSPORT_CLASS': 'path.to.your.provider',
    'CELERY': 'path.to.your.celery.file'
}
`
4. In your methods use 
+ `generate_otp` - to generate code and send it
+ `verify_otp` - to verify payload from user
 