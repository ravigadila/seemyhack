from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from hack.models import Hack


class HackForm(forms.ModelForm):
    """
    Form to enter user hack
    only title and discription are editable
    """
    def __init__(self, *args, **kwargs):
        super(HackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'myhack'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('Publish', 'Submit'))

    class Meta:
        model = Hack
        exclude = ['user', 'creation_date', 'deletion_date',
                   'last_edit', 'is_active', 'slug']
