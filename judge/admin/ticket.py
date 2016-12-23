from django.contrib.admin import ModelAdmin
from django.contrib.admin.options import InlineModelAdmin
from django.forms import ModelForm

from judge.models import TicketMessage
from judge.widgets import HeavySelect2Widget, HeavySelect2MultipleWidget, AdminPagedownWidget


class TicketMessageForm(ModelForm):
    class Meta:
        widgets = {
            'user': HeavySelect2Widget(data_view='profile_select2', attrs={'style': 'width: 100%'}),
        }
        if AdminPagedownWidget is not None:
            widgets['body'] = AdminPagedownWidget()


class TicketMessageInline(InlineModelAdmin):
    model = TicketMessage
    form = TicketMessageForm
    fields = ('user', 'body')


class TicketForm(ModelForm):
    class Meta:
        widgets = {
            'user': HeavySelect2Widget(data_view='profile_select2', attrs={'style': 'width: 100%'}),
            'assignees': HeavySelect2MultipleWidget(data_view='profile_select2', attrs={'style': 'width: 100%'}),
        }


class TicketAdmin(ModelAdmin):
    fields = ('title', 'user', 'assignees', 'content_type', 'object_id', 'notes')
    list_display = ('title', 'user', 'time', 'linked_item')
    inlines = [TicketMessageInline]
    form = TicketForm