import os
from distutils.util import strtobool
from importlib import import_module

from django.apps import AppConfig
from django.conf import settings

from drf_model_pusher.config import connect_pusher_views


class DrfModelPusherAppConfig(AppConfig):
    name = "drf_model_pusher"

    def ready(self):
        connect_pusher_views()

        pusher_backends_file = "pusher_backends.py"

        if hasattr(settings, "DRF_MODEL_PUSHER_BACKENDS_FILE"):
            pusher_backends_file = settings.DRF_MODEL_PUSHER_BACKENDS_FILE

        for app_config in self.apps.get_app_configs():
            if os.path.exists(os.path.join(app_config.path, pusher_backends_file)):
                import_module("{0}.pusher_backends".format(app_config.name))

