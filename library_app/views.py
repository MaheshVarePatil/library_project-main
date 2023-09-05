from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Member, Transaction
from .forms import BookForm, MemberForm, TransactionForm, BookImportForm, TransactionSearchForm
from django.db.models import Sum
from decimal import Decimal
import requests


def book_list(request):
    title_query = request.GET.get('title', '')
    author_query = request.GET.get('author', '')
    books = Book.objects.all()
    if title_query:
        books = books.filter(title__icontains=title_query)
    if author_query:
        books = books.filter(author__icontains=author_query)
    context = {
        'books': books,
    }

    return render(request, 'book_list.html', context)
    

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'book_create.html', {'form': form})


def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_update.html', {'form': form,"xyz":book})

def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'book_confirm_delete.html', {'book': book})


def member_list(request):
    name_query = request.GET.get('name', '')
    email_query = request.GET.get('email', '')
    members = Member.objects.all()
    if name_query:
        members = members.filter(name__icontains=name_query)
    if email_query:
        members = members.filter(email__icontains=email_query)
    context = {
        'members': members,
    }

    return render(request, 'member_list.html', context)


def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'member_form.html', {'form': form})


def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'member_form.html', {'form': form})


def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'member_confirm_delete.html', {'member': member})


def transaction_list(request):
    search_form = TransactionSearchForm(request.GET)
    book_title_query = request.GET.get('book_title', '')
    member_name_query = request.GET.get('member_name', '')
    transactions = Transaction.objects.all()
    if book_title_query:
        transactions = transactions.filter(book__title__icontains=book_title_query)
    if member_name_query:
        transactions = transactions.filter(member__name__icontains=member_name_query)
    context = {
        'transactions': transactions,
        'search_form': search_form, 
    }

    return render(request, 'transaction_list.html', context)

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.cleaned_data['rent_fee']
            transaction = form.save(commit=False)
            book = transaction.book
            rent_fee = transaction.rent_fee
            member = transaction.member
            print(member)
            if transaction.return_date:
                if rent_fee > 500 :
                    print("not accepted")
                else:
                    transaction.rent_fee = rent_fee
                    member.outstanding_debt += rent_fee
                    transaction.save()
                    member.save()  
            else:
                transaction.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transaction_form.html', {'form': form})

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            y = form.cleaned_data['rent_fee']
            if y >500:
                print("not accepted")
            else:
                form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transaction_form.html', {'form': form})


def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transaction_confirm_delete.html', {'transaction': transaction})


def book_import(request):
    user_input = request.GET.get('user_input', '')
    books_data = []

    if user_input:
        try:
            response = requests.get(f'https://frappe.io/api/method/frappe-library?page=1&title={user_input}')
            if response.status_code == 200:
                data = response.json().get('message', [])
                books_data = data
            else:
                print('API Error:', response.status_code)
        except Exception as e:
            print('Error fetching data:', str(e))

    return render(request, 'book_import.html', {'user_input': user_input, 'books_data': books_data})










