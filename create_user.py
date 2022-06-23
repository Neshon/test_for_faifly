import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_for_faifly.settings")
django.setup()


from user.models import User


def CreateUser(username, password, email, role=None, superuser=False):
    user = User(
        username=username,
        email=email,
    )
    user.set_password(password)
    user.is_superuser = superuser
    user.is_staff = True
    user.role = role
    user.save()

    return user


if __name__ == "__main__":
    CreateUser('root', 'root', 'root@root.ro', superuser=True)
    CreateUser('manager', 'manager', 'manager@manager.ma', 1)
    CreateUser('administrator', 'administrator', 'administrator@admin.ad', 2)



