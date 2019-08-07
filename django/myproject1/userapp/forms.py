from django import forms

class RegistrationForm(forms.Form):
	first_name=forms.CharField(
		label="Enter your First Name",
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'firstname'
			}
		)
	)
	last_name=forms.CharField(
		label="Enter your Last Name",
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'lastname'
			}
		)
	)
	mobile=forms.CharField(
		label="Enter your Mobile",
		widget=forms.NumberInput(
			attrs={
				'class':'form-control',
				'placeholder':'mobile'
			}
		)
	)
	email=forms.CharField(
		label="Enter your Email",
		widget=forms.EmailInput(
			attrs={
				'class':'form-control',
				'placeholder':'Email'
			}
		)
	)
	username=forms.CharField(
		label="Enter your Username",
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'Username'
			}
		)
	)
	password=forms.CharField(
		label="Enter your Password",
		widget=forms.PasswordInput(
			attrs={
				'class':'form-control',
				'placeholder':'password'
			}
		)
	)
	confirm_password=forms.CharField(
		label="Enter your Password again",
		widget=forms.PasswordInput(
			attrs={
				'class':'form-control',
				'placeholder':'confirm password'
			}
		)
	)
	
class LoginForm(forms.Form):
	username=forms.CharField(
		label="Enter your UserName",
		widget=forms.TextInput(
			attrs={
				'class':'form-control',
				'placeholder':'Username'
			}
		)
	)
	password=forms.CharField(
		label="Enter your Password",
		widget=forms.PasswordInput(
			attrs={
				'class':'form-control',
				'placeholder':'password'
			}
		)
	)

