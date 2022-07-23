from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review
from admin import ReviewAdmin


class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'isbn', 'get_publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'publisher__name')

    def get_publisher(self, obj):
        return obj.publisher.name


def initialled_name(obj):
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return f"{obj.last_names}, {initials}"


class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    search_fields = ('last_names__startswith', 'first_names')


admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
