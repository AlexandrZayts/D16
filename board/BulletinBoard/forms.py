from allauth.account.forms import SignupForm
from django import forms


from .models import Ads


class AdsForm(forms.ModelForm):
    description = forms.CharField(min_length=20)

    class Meta:
        model = Ads
        fields = ['Ads_author', 'Ads_category', 'Ads_header', 'Ads_text']


class BasicSignupForm(SignupForm):

    def save(self, requst):
        user = super(BasicSignupForm, self).save(requst)
        basic_group = Group.object.get(name='common')
        basic_group.user_set.add(user)
        return