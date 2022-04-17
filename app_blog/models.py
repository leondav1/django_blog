from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Post(models.Model):
    ACTIVE_CHOICES = [
        (True, 'active'),
        (False, 'deactive')
    ]
    title = models.CharField(verbose_name='название', max_length=500)
    description = models.TextField(verbose_name='содержание')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='дата редактирования', auto_now=True)
    active = models.BooleanField(
        verbose_name='активность',
        max_length=1,
        choices=ACTIVE_CHOICES,
        default=False
    )

    class Meta:
        ordering = ['-created_at']

    def get_comment(self):
        return self.post_comments.filter(parent__isnull=True)

    def __str__(self):
        return self.title


class PostComment(MPTTModel):
    ACTIVE_CHOICES = [
        (True, 'active'),
        (False, 'deactive')
    ]
    name = models.CharField(verbose_name='имя пользователя', max_length=100)
    user = models.ForeignKey(
        'auth.User',
        default=None,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='user_comment'
    )
    comment = models.TextField(verbose_name='комментарий')
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    post = models.ForeignKey(
        'Post',
        default=None,
        null=True,
        on_delete=models.CASCADE,
        related_name='post_comments'
    )
    parent = TreeForeignKey(
        'self',
        default=None,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='parent comment'
    )
    is_active = models.BooleanField(
        verbose_name='активность',
        max_length=1,
        choices=ACTIVE_CHOICES,
        default=False
    )

    class MPTTMeta:
        # ordering = ['-created_at']
        order_insertion_by = ['id']

    def __str__(self):
        return self.name
