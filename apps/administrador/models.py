from django.contrib.admin.models import LogEntry
from datetime import datetime, date
from django.forms import model_to_dict
from apps.utils.format_date import current_date_format
from apps.auditoria.mixins import AuditMixin


class Logs(LogEntry):
    class Meta:
        proxy = True

    def get_action_color(self):
        if self.action_flag == 1:
            return 'timeline-item-marker-indicator bg-green'
        elif self.action_flag == 2:
            return 'timeline-item-marker-indicator bg-yellow'
        else:
            return 'timeline-item-marker-indicator bg-red'

    def get_action_text(self):
        if self.action_flag == 1:
            return 'creado'
        elif self.action_flag == 2:
            return 'modificado'
        else:
            return 'eliminado'

    def get_days(self):
        current_date = date.today()
        past_date = self.action_time.date()
        days = (current_date - past_date).days
        if days == 0 or -1:
            return 'Hoy'
        elif days == 1:
            return '{} día'.format(days)
        else:
            return '{} días'.format(days)
        # return days

    def to_json(self):
        item = model_to_dict(self)
        item['user'] = self.user.__str__()
        item['date'] = current_date_format(self.action_time)
        return item
