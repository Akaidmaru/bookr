from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review
from admin import BookAdmin, ContributorAdmin, ReviewAdmin

admin.site.register(Publisher)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)
