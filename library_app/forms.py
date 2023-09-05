from django import forms
from .models import Book, Member, Transaction

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'


class BookImportForm(forms.Form):
    num_books = forms.IntegerField(
        label='Number of Books to Import', 
        min_value=1, 
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    title = forms.CharField(
        label='Title', 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    isbn = forms.CharField( 
        label='ISBN',
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    publisher = forms.CharField(  
        label='Publisher',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    authors = forms.CharField(
        label='Authors', 
        required=False, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    page = forms.IntegerField(  
        label='Page Count',
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class BookSearchForm(forms.Form):
    title = forms.CharField(
        label='Title',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Title'})
    )
    authors = forms.CharField(
        label='Authors',
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by Author'})
    )

class TransactionSearchForm(forms.Form):
    book_title = forms.CharField(
        max_length=100,
        required=False,
        label="Search by Book Title",
        widget=forms.TextInput(attrs={'placeholder': 'Search by Book Title'})
    )
    member_name = forms.CharField(
        max_length=100,
        required=False,
        label="Search by Member Name",
        widget=forms.TextInput(attrs={'placeholder': 'Search by Member Name'})
    )


