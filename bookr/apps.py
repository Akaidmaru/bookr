from django.contrib.admin.apps import AdminConfig


class BookrAdminConfig(AdminConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # name = 'reviews'
    default_site = 'admin.BookrAdminSite'
