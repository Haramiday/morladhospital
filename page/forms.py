from django import forms

choice = (("1","General CheckUp"),
		("2","Laboratory Test"),
		("3","Children Care"))

class Appointment(forms.Form):
	Name = forms.CharField()
	Email = forms.EmailField()
	Phone_Number = forms.CharField()
	Gender = forms.ChoiceField(choices = (("1","Male"),("2","Female")))
	Request_service = forms.ChoiceField(choices = choice)
	Additional_message = forms.CharField()
