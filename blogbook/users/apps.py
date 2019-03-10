from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

#accepting signals- profile section
    def ready(self):
        import users.signals
