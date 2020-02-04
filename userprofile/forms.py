from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField()
    password2 = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'email',)
    # 对两次输入的密码进行校验
    def clean_password2(self):
        data = self.cleaned_data    # cleaned_data函数根据表单字段清洗出合法数据(字典类型数据)
        pwd1 = data.get('password1')
        pwd2 = data.get('password2')
        if pwd1 == pwd2:
            return pwd1
        else:
            raise forms.ValidationError('密码一和密码二不一致，请检查。')