from accounts.models import User


def get_username(username):
    username = username
    n = 0
    while True:
        if not User.objects.filter(username=username).exists():
            break
        else:
            username = username + str(n)
        n += 1

    return username
