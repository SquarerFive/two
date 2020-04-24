from django import forms

class LoginForm(forms.Form):
    #email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    #password = forms.PasswordInput(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class GameServerForm(forms.Form):
    server_name = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    server_address = forms.CharField(max_length = 50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    server_max_players = forms.IntegerField(max_value=64, widget=forms.TextInput(attrs={'class': 'form-control'}))