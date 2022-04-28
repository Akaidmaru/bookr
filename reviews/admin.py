from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

# admin_site = BookrAdminSite(name='bookr')

admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book)
admin.site.register(BookContributor)
admin.site.register(Review)
