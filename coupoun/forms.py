from django import forms

class Codeform(forms.Form):
	code = forms.CharField(label='EnterCode:',max_length=7)
	