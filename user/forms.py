from django import forms#form classımdan register form oluşturuyoruz

class LoginForm(forms.Form):
    username = forms.CharField(label = "Kullanıcı Adı")
    password = forms.CharField(label = "Parola",widget  =forms.PasswordInput)


class RegisterForm(forms.Form):#template ta bunu gösterince inpute a dönüşüyor bu
    username = forms.CharField(max_length = 50, label = "Kullanıcı Adı")
    password = forms.CharField(max_length=20,label = "Parola",widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Parolayı Doğrula",widget = forms.PasswordInput)
    #password ile confirmin aynı olup olmadığın görmek için clean kullanıyoruz
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Parolar Eşleşmiyor")

        values= {
            "username" : username,
            "password" : password,

        }
        return values