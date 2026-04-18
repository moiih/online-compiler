from django import forms
from .models import CodeFileUpload


class CodeAreaForm(forms.Form):

    PROG_LANG_CHOICE = (
        ('C', 'C'),
        ('C++', 'C++'),
        ('Python3', 'Python3'),
        ('Java', 'Java'),
    )

    prog_lang = forms.TypedChoiceField(choices = PROG_LANG_CHOICE)    
    
    code = forms.CharField(
        widget = forms.Textarea(attrs={'class':'form-control col-4', 'rows':'7'}),
        label = 'Enter Your Code Here',        
    )

    filename = forms.CharField(required=False)


class InputsForm(forms.Form):

    inputs = forms.CharField(
        widget = forms.Textarea(attrs={'class':'form-control col-4', 'rows':'3', 'id':'area'}),
        label = 'Inputs(if any)',
        required = False
    )


# class SaveFileForm(forms.Form):

#     filename = forms.CharField()


class CodeUploadForm(forms.ModelForm):

    class Meta:
        model = CodeFileUpload
        fields = [ 'codefile' ]