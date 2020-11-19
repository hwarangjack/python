from django import forms

class post_form(forms.Form):
    # who = models.CharField()
    # text = models.TextField())
    # picture = models.ImageField()
    # date = models.DateTimeField()
    who = forms.CharField(max_length=5)
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'작성하고자 하는 글을 입력하세요','row':4,'col':10}))
    picture = forms.ImageField()
    date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder':'YYYY-MM-DD'}))
