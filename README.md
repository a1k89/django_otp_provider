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
1. `pip install django-otp-provider`
2. Create your custom class extends from `BaseTransport` and implement `send_code` method
3. In settings.py:
```python
OTP_PROVIDER = {
    'TRANSPORT_TYPE': "SMS", # EMAIL/SMS
    'TRANSPORT_CLASS': 'path.to.your.provider',
    'CELERY': 'path.to.your.celery.file' # Send code async
}
```
4. Then, in your code you may to use: 
+ `generate_otp` - to generate code and send it
+ `verify_otp` - to verify payload from user
