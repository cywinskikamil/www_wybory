from django.contrib import admin
from django import forms
# Register your models here.

from .models import Gmina, Wojewodztwo, Kandydat, WojewodztwoRozmiar, WojewodztwoRodzaj


class GminaForm(forms.ModelForm):
    class Meta:
        model = Gmina
        fields = '__all__'

    def clean(self):
        lm = self.cleaned_data.get('liczba_mieszkancow')
        lu = self.cleaned_data.get('liczba_uprawnionych')
        lw = self.cleaned_data.get('liczba_wydanych_kart')
        lo1 = self.cleaned_data.get('liczba_glosow_oddanych_na_kandydata_nr_1')
        lo2 = self.cleaned_data.get('liczba_glosow_oddanych_na_kandydata_nr_2')

        if not lm or not lu or not lw or not lo1 or not lo2:
            raise forms.ValidationError("Ktoreś z wymaganych pól nie zostało wypelnione")

        # liczba oddanych glosow razem
        lor = lo1 + lo2

        if lm < 0 or lo1 < 0 or lo2 < 0:
            raise forms.ValidationError("ujemna liczba głosów zakazana")

        if lm < lu:
            raise forms.ValidationError("liczba mieszkańców nie może być mniejsza od iczby uprawnionych")
        if lu < lw:
            raise forms.ValidationError("liczba uprawnionych nie może być mniejsza od liczby wydanych kart")
        if lw < lor:
            raise forms.ValidationError("liczba wydanych kart nie może być mniejsza od \
                                        liczby otrzymanych przez kandydatów głosów")
        if lor != lo1 + lo2:
            raise forms.ValidationError("liczba otrzymanych przez kandydatów głosów nie \
                                         może być mniejsza od liczby ważnych głosów")
        return self.cleaned_data


class GminaAdmin(admin.ModelAdmin):
    form = GminaForm
    list_display = ('nazwa', 'rodzaj', 'liczba_mieszkancow')


class KandydatAdmin(admin.ModelAdmin):
    list_display = ('imie', 'nazwisko')

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 2:
            return False
        else:
            return True


class WojewodztwoAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 16:
            return False
        else:
            return True

admin.site.register(Wojewodztwo, WojewodztwoAdmin)
admin.site.register(Kandydat, KandydatAdmin)
admin.site.register(Gmina, GminaAdmin)
admin.site.register(WojewodztwoRodzaj)
admin.site.register(WojewodztwoRozmiar)


