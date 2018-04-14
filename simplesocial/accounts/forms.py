from django.contrib.auth import get_user_model # returns the usermodel that is currently active in this project
from django.contrib.auth.forms import UserCreationForm  # built into auth package.  This has good documentation. Admin accounts user accounts


class UserCreateForm(UserCreationForm):  # make sure the import and this class to have the exact same NAME

    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = "Email Address"

        # not necessary
        # user comes in calls UserCreationForm, then we setup the meta class saying these are the fields I want the user to have access to.
