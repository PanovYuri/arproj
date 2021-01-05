from django import forms

class CardForm(forms.Form):
    title = forms.CharField(
        max_length=200, 
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "Название"}))
    description = forms.CharField(
        max_length=500, 
        widget=forms.TextInput(
            attrs={"class": "input", "placeholder": "Описание"}))
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={"class": "input", "placeholder": "Ссылка не мероприятие", "type": "url"}))
    date_event = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"class": "input", "placeholder": "Дата мероприятия", "type": "date"}))

class FileUploadForms(forms.Form):
    media = forms.FileField(
        widget=forms.FileInput(
            attrs={"class": "file-input"}
        )
    )