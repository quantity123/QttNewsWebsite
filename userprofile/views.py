from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegisterForm
from django.views.generic import RedirectView

class Login(RedirectView):
    def get(self, request, *args, **kwargs):
        if self.request.method == 'POST':
            userLoginForm = UserLoginForm(data=self.request.POST)
            if userLoginForm.is_valid():
                # cleaned_data函数根据表单字段清洗出合法数据(字典类型数据)
                data = userLoginForm.cleaned_data
                # 验证账户和密码能否匹配数据库中的某一个用户
                userr = authenticate(username=data.get('username'), password=data['password'])  # data['name'] 取值如果没有name属性将报错, data.get()就不会报错
                if userr:
                    # 保存到seesion
                    login(self.request, userr)
                    # return HttpResponseRedirect(reverse('article:home'))
                    return redirect('article:home')
                else:
                    return HttpResponse('账户或密码不正确，请修改。')
            else:
                return HttpResponse('账号或密码输入不合法')
        elif self.request.method == 'GET':
            userLoginForm = UserLoginForm()
            context = {'form': userLoginForm}
            return render(self.request, 'userprofile/login.html', context)
        else:
            return HttpResponse('只能使用POST或GET请求数据。')

class Logout(RedirectView):
    def get(self, request, *args, **kwargs):
        # 清除seesion
        logout(request)
        return redirect('article:home')

class Register(RedirectView):
    def get(self, request, *args, **kwargs):
        if request.method == 'POST':
            userRegisterForm = UserRegisterForm(data=request.POST)
            if userRegisterForm.is_valid():
                newUser = userRegisterForm.save(commit=False)
                data = userRegisterForm.cleaned_data
                pwd = data.get('password1')
                newUser.set_password(pwd)
                newUser.save()
                if request.user.is_authenticated:
                    logout(request)
                login(request, newUser)
                return redirect('article:home')
            else:
                return HttpResponse('注册表单有错误。')
        elif request.method == 'GET':
            userRegisterForm = UserRegisterForm()
            context = {'userRegisterForm': userRegisterForm}
            return render(request, 'userprofile/register.html', context)
        else:
            return HttpResponse('请使用GET或POST请求。')