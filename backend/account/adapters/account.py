from allauth.account.adapter import DefaultAccountAdapter
from extra_settings.models import Setting


class AccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        is_open = Setting.get("ACCOUNT_IS_OPEN_FOR_SIGNUP")
        if not isinstance(is_open, bool):
            raise ValueError("ACCOUNT_IS_OPEN_FOR_SIGNUP must be a boolean.")
        return is_open
