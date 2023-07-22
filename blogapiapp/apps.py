from django.apps import AppConfig


class BlogapiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogapiapp'
    
    def ready(self):
        import blogapiapp.signals
       
