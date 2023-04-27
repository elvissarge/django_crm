from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
		self.fields['first_name'].label = ''
		self.fields['first_name'].help_text = '<span class="form-text text-muted"><small>Required.</small></span>'

		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
		self.fields['last_name'].label = ''
		self.fields['last_name'].help_text = '<span class="form-text text-muted"><small>Required.</small></span>'

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required.</small></span>'

		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = 'Email'
		self.fields['email'].label = ''
		self.fields['email'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	

class AddRecordForm(forms.ModelForm):
	#first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}),label="")
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.CharField(required=True)
	phone = forms.CharField(required=True)
	address = forms.CharField(required=True)
	city = forms.CharField(required=True)
	state = forms.CharField(required=True)
	zipcode = forms.CharField(required=True)

	class Meta:
		model = Record
		exclude = {"user",}