from django.conf import settings
import requests


def get_client_ip(request):
    x_forwarded_for =  request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')


def recaptcha_verify(request):

    if request.method == 'POST':
        response = {}
        data =  request.POST
        captcha_rs = data.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        params = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': captcha_rs,
            'remoteip': get_client_ip(request)
        }

        verify_rs =  requests.get(url, params=params, verify=True)

        print(verify_rs)
        verify_rs_json = verify_rs.json()

        return verify_rs_json['success']
    