import time

from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from user.models import UserProfile, PersonalProfile


class Login(View):
    @csrf_exempt
    def get(request):
        return render(request, "login/login.html")

    @csrf_exempt
    @require_http_methods(["POST"])
    def post(request):
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        macpw = make_password(pass_word, "importlib", 'pbkdf2_sha256')
        # 实例化用户，然后赋值
        user = auth.authenticate(username=user_name, password=pass_word)

        if user is not None:
            if user.is_active:
                login(request, user)
                # 更新最后登录时间
                now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                user.last_login = now_time
                user.save(force_update=True)
                request.session["user_id"] = user.id
                return HttpResponseRedirect("userauth/index.html")

        return HttpResponseRedirect('/login.html')


@login_required
def index(request):
    user_id = request.session.get('user_id')
    try:
        user = UserProfile.objects.get(id=user_id)
    except:
        user = PersonalProfile.objects.get(id=user_id)
    return render(request, "userauth/index.html", {"user": user, "article": article})
