from django import forms
class ProductForm(forms.Form):
    pid=forms.IntegerField(label='Enter pid')
    pname=forms.CharField(label="Enter pname",max_length=20)
    pcost=forms.DecimalField(label="enter pcost",max_digits=10,
                             decimal_places=4)
    pmfd=forms.DateField(label="Enter pmfd")
    pexpdt=forms.DateField(label="Enter pexpdt")
