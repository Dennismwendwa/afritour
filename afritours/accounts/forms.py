from datetime import date
from django import forms
from . models import Contact


class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ('name', 'email', 'subject', 'message', )



	"""
	name = forms.CharField(max_length=250)
	email = forms.EmailField()
	feedback = forms.ChoiceField(choices=[('1', 'Feedback'), ('2', 'Report a bug'),
			('3', 'Feature request'), ('4', 'Other')])
	date = forms.DateField(initial=date.today, widget=forms.HiddenInput)
	message = forms.CharField(widget=forms.Textarea)
	"""
