from django.test import TestCase
from apps.usuario.models import User


class TestUser(TestCase):
    def setUp(self) -> None:
        User.objects.create(
            username='0401798475001',
            email='anderam92@test.com',
            first_name='Anderson Ramiro',
            last_name='Pozo Imbaquingo',
            is_active=True,
            is_staff=False,
            is_superuser=True,
        )

    def test_user_is_admin(self):
        usuario = User.objects.get(username='0401798475001')
        self.assertTrue(usuario.is_superuser, True)

    def test_user_is_active(self):
        usuario = User.objects.get(username='0401798475001')
        self.assertTrue(usuario.is_active, True)

    def test_user_is_staff(self):
        usuario = User.objects.get(username='0401798475001')
        self.assertFalse(usuario.is_staff, False)

    def test_get_name_avatar(self):
        usuario = User.objects.get(username='0401798475001')
        self.assertEqual(usuario.avatar_name(), 'AP')

    def test_check_password(self):
        usuario = User.objects.get(username='0401798475001')
        usuario.set_password('0401798475')
        is_correct_password = usuario.check_password('0401798475')
        self.assertEqual(is_correct_password, True)
