from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from guardian.conf import settings as guardian_settings
from guardian.mixins import GuardianUserMixin


class User(GuardianUserMixin, AbstractUser):
    first_name = None
    last_name = None

    display_name = models.CharField(
        _("Display Name"),
        max_length=255,
        blank=True,
        null=True,
    )

    REQUIRED_FIELDS = AbstractUser.REQUIRED_FIELDS + ["display_name"]

    def __str__(self):
        return self.display_name

    class Meta(AbstractUser.Meta):
        pass

    @property
    def is_anonymous(self):
        # django-guardian が提供する匿名ユーザーの名前と一致する場合は匿名ユーザーとして扱う
        anon_username = guardian_settings.ANONYMOUS_USER_NAME
        username = self.get_username()
        if username and anon_username and username == anon_username:
            return True

        return super().is_anonymous

    @property
    def is_authenticated(self):
        # 匿名ユーザーでないことを確認する
        return super().is_authenticated and not self.is_anonymous
