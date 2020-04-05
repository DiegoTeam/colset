from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'apps.users'

    def ready(self):
        self.index_name = 'Usuarios'
        self.icon = 'accessibility'
        self.url = ''
        self.permisos = {
            'users.usuarios'
        }
        self.menu = [
            {
                'name': 'Cuentas',
                'permiso': 'users.cuentas',
                'url': '',
                'status': '',
                'other_urls': [],
                'submenu': [
                    {
                        'name': 'Submenu cuentas',
                        'permiso': 'users.cuentas',
                        'url': '',
                        'status': '',
                        'other_urls': []
                    },
                ]
            },
            {
                'name': 'Roles',
                'permiso': 'users.roles',
                'url': '',
                'status': '',
                'other_urls': [],
                'submenu': []
            },
            {
                'name': 'Permisos',
                'permiso': 'users.permisos',
                'url': '',
                'other_urls': [],
                'status': '',
                'submenu': []
            }
        ]
