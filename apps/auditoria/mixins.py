from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION
from django.utils.encoding import force_str
from datetime import datetime


class AuditMixin(object):
    def save_log(self, user, message, action):
        log = LogEntry.objects.create(
            user_id=user.id,
            action_time=datetime.now(),
            content_type_id=ContentType.objects.get_for_model(self).id,
            object_id=self.id,
            object_repr=force_str(self),
            action_flag=action,
            change_message=message,
        )

    def save_addition(self, user):
        self.save_log(user, 'Agregado', ADDITION)

    def save_edition(self, user):
        self.save_log(user, 'Modificado', CHANGE)

    def save_deletion(self, user):
        self.save_log(user, 'Eliminado', DELETION)
