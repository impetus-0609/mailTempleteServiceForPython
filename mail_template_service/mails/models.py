from django.db import models


class Employee(models.Model):
    """
    社員データ
    """
    id = models.CharField(
        verbose_name='社員番号',
        max_length=128,
        primary_key=True,
    )

    name = models.CharField(
        verbose_name='社員名',
        max_length=128,
        null=False,
        blank=False,
    )

    mail_address = models.EmailField(
        verbose_name='メールアドレス',
        max_length=128,
    )

    def __str__(self):
        return '{}:{}'.format(self.id, self.name)
