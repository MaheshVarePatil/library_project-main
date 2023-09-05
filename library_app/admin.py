from django.contrib import admin
from .models import Book, Member, Transaction

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publisher', 'page_count', 'stock')
    list_filter = ('publisher',)
    search_fields = ('title', 'author', 'isbn')
    list_per_page = 20

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'outstanding_debt')
    search_fields = ('name', 'email')
    list_per_page = 20

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('book', 'member', 'issue_date', 'return_date', 'rent_fee')
    list_filter = ('issue_date', 'return_date')
    search_fields = ('book__title', 'member__name')
    list_per_page = 20

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['rent_fee', 'return_date']
        return []

    def save_model(self, request, obj, form, change):
        if change and obj.return_date:
            days_diff = (obj.return_date - obj.issue_date).days
            rent_fee = days_diff * 10.00 
            obj.rent_fee = rent_fee
            obj.member.outstanding_debt += rent_fee
            obj.member.save()
        obj.save()

