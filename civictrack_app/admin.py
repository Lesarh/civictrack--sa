from django.contrib import admin
from django.utils.html import format_html
from .models import Report, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('sender', 'text', 'created_at')
    readonly_fields = ('sender', 'text', 'created_at')
    can_delete = False


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'location')

    fields = (
        'title',
        'description',
        'location',
        'latitude',
        'longitude',
        'image_preview',
        'image',
        'status',
        'created_at',
    )

    readonly_fields = (
        'title',
        'description',
        'location',
        'latitude',
        'longitude',
        'image_preview',
        'image',
        'created_at',
    )

    inlines = [CommentInline]

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="250" style="border-radius:8px;" />',
                obj.image.url
            )
        return "No image uploaded"

    image_preview.short_description = "Image Preview"

    def has_add_permission(self, request):
        return False


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('report', 'sender', 'text', 'created_at')
    list_filter = ('sender', 'created_at')
    search_fields = ('report__title', 'text')

    fields = ('report', 'sender', 'text', 'created_at')
    readonly_fields = ('created_at',)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.sender = 'Admin'
        super().save_model(request, obj, form, change)