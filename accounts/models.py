from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

# from django.db.models.signals import post_save
# from django.dispatch import receiver


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """Custom User model"""

    username = None
    email = models.EmailField(_('email address'), unique=True)
    role = models.ForeignKey('UserRole', on_delete=models.CASCADE, default=2)
    watchlist = models.ManyToManyField(
        'tickets.Ticket', related_name="%(class)s_watchlist", null=True, blank=True)
    created_tickets = models.ManyToManyField(
        'tickets.Ticket', related_name="%(class)s_created_tickets", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class UserRole(models.Model):
    label_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.label_name


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_image = models.IntegerField(blank=True)
#     location = models.CharField(max_length=30, blank=True)


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
