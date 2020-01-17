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


class Unit(models.Model):
    """
    ユニット
    """
    CHOICE_UNIT = (
        ('1', 'ユニット1'),
        ('2', 'ユニット2'),
    )
    name = models.CharField(
        verbose_name='ユニット名',
        max_length=5,
        choices=CHOICE_UNIT,
        unique=True,
    )


class Team(models.Model):
    """
    チーム
    """
    name = models.CharField(
        verbose_name='チーム名',
        max_length=128,
        unique=True,
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
    )


class Section(models.Model):
    """
    セクション
    """
    name = models.CharField(
        verbose_name='セクション名',
        max_length=128,
        unique=True,
    )

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
    )


class MailTemplete(models.Model):
    """
    メールテンプレート
    元となる本文情報を保持.
    """

    type = models.CharField(
        verbose_name='メール種別',
        max_length=128,
        unique=True,
    )

    text = models.TextField(
        verbose_name='本文',
        null=True,
        blank=True,
        max_length=1000,
    )

    # TODO 選択時にフィルインする種別とかの設定





