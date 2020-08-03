from .models import Person, Lesson
from bootstrap_modal_forms.forms import BSModalModelForm


class PersonModelForm(BSModalModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number', 'lessons']
