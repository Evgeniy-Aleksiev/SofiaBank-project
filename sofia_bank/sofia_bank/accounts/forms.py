from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.core.validators import MinLengthValidator

from sofia_bank.accounts.models import Profile
from sofia_bank.common_files.helpers import BootstrapFormMixin
from sofia_bank.common_files.validators import validate_only_letters, validate_age, validate_only_numbers


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(Profile.FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    middle_name = forms.CharField(
        max_length=Profile.MIDDLE_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(Profile.MIDDLE_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(Profile.LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    egn = forms.CharField(
        max_length=10,
        validators=(
            MinLengthValidator(10),
            validate_only_numbers,
        )
    )

    email = forms.EmailField()

    mobile_number = forms.CharField(
        max_length=9,
        validators=(
            MinLengthValidator(8),
            validate_only_numbers,
        )
    )

    date_of_birth = forms.DateField(validators=(
            validate_age,
        )
    )

    gender = forms.ChoiceField(
        choices=Profile.GENDERS,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            middle_name=self.cleaned_data['middle_name'],
            last_name=self.cleaned_data['last_name'],
            egn=self.cleaned_data['egn'],
            email=self.cleaned_data['email'],
            mobile_number=self.cleaned_data['mobile_number'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'middle_name', 'last_name', 'username', 'egn',
                  'email', 'mobile_number', 'date_of_birth', 'gender')
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name',
                }
            ),
            'middle_name': forms.TextInput(
                attrs={
                    'placeholder': 'Middle name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                }
            ),
            'egn': forms.TextInput(
                attrs={
                    'placeholder': 'EGN',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }
            ),
            'mobile_number': forms.TextInput(
                attrs={
                    'placeholder': 'Mobile number',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'Date of birth',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'placeholder': 'gender',
                }
            ),
        }


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()
        self.initial['gender'] = Profile.DO_NOT_SHOW

    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    pass



