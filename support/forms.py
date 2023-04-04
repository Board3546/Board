import logging

from django import forms

from questionnaire.forms import BootstrapStylesMixin
from support.models import Ticket, SiteReview

logger = logging.getLogger("main")


class CreateTicketForm(BootstrapStylesMixin, forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["user", "question", "status"]


class CreateSiteReviewForm(BootstrapStylesMixin, forms.ModelForm):
    class Meta:
        model = SiteReview
        fields = ["rate", "comment", "wishes", "created_by"]

    def clean(self):
        super(CreateSiteReviewForm, self).clean()
        if not self.errors:
            user = self.cleaned_data.get("created_by")
            logger.error(
                {
                    "message": f'Пользователь "{user}" оставил отзыв с оценкой "{self.cleaned_data.get("rate")}": \n{self.cleaned_data.get("comment")}\n и пожелания: {self.cleaned_data.get("wishes")}',
                    "mail_needed": True,
                }
            )
