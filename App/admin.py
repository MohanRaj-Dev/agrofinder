from django.contrib import admin
from App.models import Fertilizer, Crops, District_L, Rates, Product
from django.db import models
from .models import District_L
from ckeditor.widgets import CKEditorWidget  # Import CKEditorWidget if using CKEditor

class Editor(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.register(Fertilizer, Editor)
admin.site.register(Crops)
admin.site.register(Rates)
admin.site.register(Product)


admin.site.register(District_L, Editor)
