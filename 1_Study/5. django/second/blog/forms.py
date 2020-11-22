from django import forms
from .models import post

class post_form(forms.Form):
    who  = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder':'아이디를 입력하세요'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'작성하고자 하는 글을 입력하세요','row':4,'col':10}))
    Upload_file = forms.FileField(required=False)
    # date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}))  # 날짜 Model에서 auto_now_add 기능을 추가했으므로 수동기재 불필요