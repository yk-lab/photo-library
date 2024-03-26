from logging import getLogger

from allauth.account.forms import LoginForm as AllauthLoginForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Field, Layout
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from libs.form_layout import Submit

logger = getLogger(__name__)


class LoginForm(AllauthLoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["login"].widget.attrs["autofocus"] = True
        self.fields["login"].required = False
        self.fields["password"].required = False

        self.fields["password"].help_text = format_html(
            '<span class="prose prose-sm prose-a:text-cyan-600 prose-a:no-underline hover:prose-a:underline">{}</span>',
            self.fields["password"].help_text,
        )

    @property
    def helper(self):
        helper = FormHelper()
        helper.layout = Layout(
            "login",
            "password",
            Field(
                "remember",
                wrapper_class="flex items-center gap-3",
                css_class="mb-2 h-4 w-4 rounded border-gray-300 text-cyan-500",
            ),
            HTML(
                """
                {% if redirect_field_value %}
                <input type="hidden" name="{{ redirect_field_name }}" value="{{ redirect_field_value }}" />
                {% endif %}
            """
            ),
            Submit("submit", _("Sign In")),
        )
        return helper
