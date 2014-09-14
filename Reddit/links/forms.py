from django.forms import ModelForm
from links.models import Link 

# Create the form class.
class LinkForm(ModelForm):
    class Meta:
        model = Link
        exclude = ('positive_votes','negative_votes')