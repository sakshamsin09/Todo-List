from django.forms import ModelForm
from app.models import TODO, Contact



class TODOForm(ModelForm):
    class Meta:
        model=TODO
        fields = ['title' ,'status', 'priority']


class CONTACTForm(ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
