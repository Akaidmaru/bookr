from django.contrib import admin


class BookrAdminSite(admin.AdminSite):
    title_header = 'Bookr Admin'
    site_header = 'Bookr administration'
    index_title = 'Bookr site admin'


# class BookAdmin(admin.ModelAdmin):
#    list_display = ('title', 'isbn')

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn', 'publisher__name__startswith')

#    def isbn13(self, obj):
#        """ '9780316769174' => '978-0-31-676917-4' """
#        return f"{obj.isbn[0:3]}-{obj.isbn[3:4]}-{obj.isbn[4:6]}-{obj.isbn[6:12]}-{obj.isbn[12:13]}"


# def initialled_name(obj):
#     """obj.first_names='Jerome David', obj.last_names='Salinger' => 'Salinger, JD'"""
#     initials = ''.join([name[0] for name in obj.first_names.split(' ')])
#     return f"{obj.last_names}, {initials}"

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')


class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',)
    # fields = ('content', 'rating', 'creator', 'book')
    fieldsets = (None, {'fields': ('creator', 'book')}), \
                ('Review content', {'fields': ('content', 'rating')})
