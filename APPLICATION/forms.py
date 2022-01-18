from django import forms #On importe la classe form de django pour gerer les formulaires


class SigninForm(forms.Form):
    your_name = forms.CharField(max_length = 50)
    your_surname = forms.CharField(max_length = 50)
    your_email = forms.CharField(max_length = 50)
    your_pass = forms.CharField(max_length = 50)
    your_role = forms.CharField(max_length = 50)
    your_matricule = forms.CharField(max_length = 9)
    your_branch = forms.CharField(max_length = 50)
    your_level = forms.CharField(max_length = 50)
    your_department = forms.CharField(max_length = 50)
    your_status = forms.CharField(max_length = 50)
    
