import requests
import json
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect


def fb_login_url():
    params = {
        'client_id': '1963632580549769',
        'client_secret': '3fc96c5eb7d2a67f6a76f16c28a201c8',
        'redirect_uri': 'http://pc.muic.uz/auth/fb',
        'response_type': 'code',
    }
    url = 'https://www.facebook.com/dialog/oauth'
    return url, params


def fb(request):
    import urllib.parse
    url, params = fb_login_url()
    redirect_uri = urllib.parse.quote(settings.FACEBOOK_REDIRECT_URI)
    fb_url = url + f'?client_id={settings.FACEBOOK_CLIENT_ID}&redirect_uri={redirect_uri}' \
                   f'&response_type=code'
    code = request.GET.get('code')
    if code:
        code = urllib.parse.quote(code)
        url = f'https://graph.facebook.com/oauth/access_token?client_id={settings.FACEBOOK_CLIENT_ID}' \
              f'&client_secret={settings.FACEBOOK_CLIENT_SECRET}&redirect_uri={redirect_uri}&code={code}'
        res = requests.get(url)
        token = json.loads(res.text)
        if token:
            token = urllib.parse.quote(token['access_token'])
            get_info_url = f'https://graph.facebook.com/me?fields=id,first_name,last_name,name,email,' \
                           f'gender,locale,picture&client_id={settings.FACEBOOK_CLIENT_ID}' \
                           f'&client_secret={settings.FACEBOOK_CLIENT_SECRET}&code={code}&access_token={token}'
            resp = requests.get(get_info_url)
            data = json.loads(resp.text)
            user = create_user_fb(data)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect('/')
        return HttpResponseRedirect('/')
    return HttpResponse(f'<a href="{fb_url}">facebook</a>')


def create_user_fb(data):
    """
    User emailga tekshiriladi agar mavjud bo`lmasa yangi User yaratiladi
    Agar ko'rsatilgan emailli User mavjud bo'lsa, uni login qilamiz
    """
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    try:
        u = User.objects.get(email=email)
        return u
    except User.DoesNotExist:
        pass
    user = User.objects.filter(Q(username=first_name.lower()) | Q(username=first_name))
    if not user.count() > 0:
        u = User(username=first_name.lower(), email=email, first_name=first_name, last_name=last_name)
        u.save()
        return u
    else:
        u = User(username=f'{first_name.lower()}_{email.split("@")[0]}',
                 email=email, first_name=first_name, last_name=last_name)
        u.save()
        return u
