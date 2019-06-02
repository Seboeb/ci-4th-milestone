from django.contrib.auth.models import User


class EmailAuth:
    """ Authenticate a user by providing an email and password """

    def authenticate(self, username=None, password=None):
        """ Get an instance of `User` based off the email and check the password """

        try:
            print(username)
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            print('hoi')
            return None

    def get_user(self, user_id):
        """ Used by django authentication system to retrieve a user instance """

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None