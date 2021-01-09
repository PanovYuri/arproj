from django import forms

class CardForm(forms.Form):
    title = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "Название"}
        )
    )
    description = forms.CharField(
        max_length=500, 
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "Описание"}
        ), 
        required=False
    )
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={"class": "input", "placeholder": "Ссылка не мероприятие", "type": "url"}
        ), 
        required=False
    )
    date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"class": "input", "placeholder": "Дата мероприятия", "type": "date"}
        ), 
        required=False
    )
    time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={"class": "input", "placeholder": "Время мероприятия", "type": "time"}
        ), 
        required=False
    )

class FileUploadForms(forms.Form):
    media = forms.FileField(
        widget=forms.FileInput(
            attrs={"class": "file-input"}
        )
    )