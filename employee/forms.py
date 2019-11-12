from django import forms
from employee.models import Employee

class EmployeeForm(forms.ModelForm):
    eid = forms.CharField(max_length=20, required=True)
    ename = forms.CharField(max_length=20, required=True)
    eemail = forms.EmailField( required=True)
    econtact = forms.IntegerField(required=True)
    gender = forms.CharField(max_length=20, required=True)
    #country = forms.CharField(max_length=25, required=True)
    #state = forms.CharField(max_length=20, required=True)
    languages = forms.CharField(max_length=20)
    #eimage = forms.FileField()




    class Meta:
        model = Employee
        fields = ("eid","ename","eemail","econtact","gender","languages","eimage")

    def save(self, commit=True):
        employee = super(EmployeeForm, self).save(commit=False)
        employee.eemail = self.cleaned_data['email']
        if commit:
            employee.save()
        return employee