from django import forms

class LectureForm(forms.Form):
    size = 15
    department = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'size': size}))
    number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'size': size}))
    name = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'size': size}))
    teacher = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'size': size}))
    time = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'size': size}))
    room = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'size': size}))
    remark = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'size': size}))

    