from django.shortcuts import redirect


def authorization_check(func):
    def decorator(request, *args, **kwargs):
        print('DECORATOR')
        user = request.user
        print(user, user.is_authenticated)
        if not user.is_authenticated:
            print('HELLLO')
            return redirect('/login')
        return func(request, *args, **kwargs)
    return decorator
