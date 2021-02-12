from .middleware import RequestMiddleware
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save)
def audit_log(sender, instance, created, raw, **kwargs):
    list_models = ['Multa', 'Juridico', ]

    if sender.__name__ not in list_models:
        return

    user = get_user()
    if created:
        instance.save_addition(user)
    elif not raw:
        instance.save_edition(user)


@receiver(post_delete)
def audit_delete_log(sender, instance, **kwargs):
    list_models = ['Multa', ]

    if sender.__name__ not in list_models:
        return

    user = get_user()
    instance.save_deletion(user)


def get_user():
    thread_local = RequestMiddleware.thread_local
    if hasattr(thread_local, 'user'):
        user = thread_local.user
        print(user)
    else:
        user = None
    return user