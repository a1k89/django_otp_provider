import importlib

from .conf import conf
from . import selectors as otp_sel

celery_conf = importlib.import_module(conf.CELERY)
app = getattr(celery_conf, "app")


@app.task
def otp_transport_handler(pk: int):
    otp = otp_sel.get_otp_by_key(pk=pk)
    if otp is None:
        return

    transport = conf.TRANSPORT
    transport.handler()


