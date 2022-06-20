from django.contrib.auth.models import BaseUserManager

# NomeDaModel.objects.create, .filter, .all


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):

        if not email:
            raise ValueError("email precisa ser passado")

        email = self.normalize_email(email)

        user = self.model(email=email, is_staff=True, is_superuser=True, **extra_fields)

        # password
        user.set_password(password)

        user.save(using=self._db)

        return user
