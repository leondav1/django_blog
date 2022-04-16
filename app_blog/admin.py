from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

from .models import Post, PostComment


class PostCommentInLine(admin.StackedInline):
    model = PostComment


class MarkGeneral(admin.ModelAdmin):
    def mark_as(self, request, queryset, active):
        updated = queryset.update(active=active)
        text = 'activated' if active else 'deactivated'
        self.message_user(request, ngettext(
            '%d story was successfully marked as {}.'.format(text),
            '%d stories were successfully marked as {}.'.format(text),
            updated,
        ) % updated, messages.SUCCESS)


@admin.register(Post)
class PostAdmin(MarkGeneral):
    list_display = ['title', 'created_at', 'active']
    inlines = [PostCommentInLine]
    list_filter = ['active']

    actions = ['mark_as_active', 'mark_as_deactive']

    def mark_as_active(self, request, queryset):
        queryset.update(active=True)

    def mark_as_deactive(self, request, queryset):
        queryset.update(active=False)

    mark_as_active.short_description = 'Перевести в статус Активно'
    mark_as_deactive.short_description = 'Перевести в статус Неактивно'


@admin.register(PostComment)
class PostCommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'get_comment', 'parent', 'level', 'is_active']
    list_filter = ['name', 'is_active']

    actions = ['mark_as_delete', 'mark_as_active', 'mark_as_deactive']

    def mark_as_delete(self, request, queryset):
        updated = queryset.update(comment='Удалено администратором!')
        self.message_user(request, ngettext(
            '%d comment was successfully marked as deleted.',
            '%d comments were successfully marked as deleted.',
            updated,
        ) % updated, messages.SUCCESS)

    def mark_as_active(self, request, queryset):
        queryset.update(is_active=True)

    def mark_as_deactive(self, request, queryset):
        queryset.update(is_active=False)

    mark_as_active.short_description = 'Перевести в статус Активно'
    mark_as_deactive.short_description = 'Перевести в статус Неактивно'

    def get_comment(self, obj):
        if len(obj.comment) > 15:
            return f'{obj.comment[:15]}...'
        return obj.comment

    get_comment.short_description = "comment"
    mark_as_delete.short_description = 'Удалить комментарий'

