from .middleware import RequestMiddleware
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# list_models = []

list_models = ['Juridico',
               'Natural',
               'Establecimiento',
               'TipoActividad',
               'Impuesto',
               'Multa',
               'Vencimiento',
               'Alcabala',
               'Plusvalia',
               'Patente',
               'DetallePatente',
               'Grupo',
               'User']


@receiver(post_save)
def audit_log(sender, instance, created, raw, **kwargs):

    if sender.__name__ not in list_models:
        return

    user = get_user()

    if user is None:
        return
    if created:
        instance.save_addition(user)
    elif not raw:
        instance.save_edition(user)


@receiver(post_delete)
def audit_delete_log(sender, instance, **kwargs):

    if sender.__name__ not in list_models:
        return

    user = get_user()

    if user is None:
        return

    instance.save_deletion(user)


def get_user():
    thread_local = RequestMiddleware.thread_local
    if hasattr(thread_local, 'user'):
        user = thread_local.user
    else:
        user = None
    return user
