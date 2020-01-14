from django import forms

class Search(forms.Form):
    name = forms.CharField(max_length=255, label='Название проекта')
    sortBy = forms.CharField(max_length=255, label='Сортировка поиска')
    showBy = forms.CharField(max_length=255, label='Показать по')
    costFrom = forms.IntegerField(min_value=0, label='Стоимости проекта с')
    costTo = forms.IntegerField(min_value=450, label='Стоимости проекта до')