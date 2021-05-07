from django.test import TestCase
from apps.usuario.models import User


class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='0401798475',
            email='anderam92@test.com',
            first_name='Anderson Ramiro',
            last_name='Pozo Imbaquingo',
            is_active=True,
            is_staff=False,
            is_superuser=True,
        )

    usuario = User.objects.get(username='0401798475')

    def test_user_is_admin(self):
        self.assertTrue(self.usuario.is_superuser, True)

    def test_user_is_active(self):
        self.assertTrue(self.usuario.is_active, True)

    def test_user_is_staff(self):
        self.assertTrue(self.usuario.is_staff, False)

    def test_get_name_avatar(self):
        self.assertEqual(self.usuario.avatar_name(), 'AP')

    def test_check_password(self):
        self.usuario.set_password('0401798475')
        is_correct_password = self.usuario.check_password('0401798475')
        self.assertEqual(is_correct_password, True)
