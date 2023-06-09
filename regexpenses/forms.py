from django import forms
from regexpenses.models import expenses


class regExp(forms.ModelForm):
    class Meta:
        model = expenses
        fields = ['cat','subject','description','amt','amtdate']
        labels = {'cat':'분류','subject':'제목', 'description':'상세','amt':' 지출금액','amtdate':'지출일자'}




