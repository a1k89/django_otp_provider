import importlib

from .conf import conf
from . import selectors as otp_sel

celery_conf = importlib.import_module(conf.CELERY)
app = getattr(celery_conf, "app")


@app.task
def otp_transport_handler(pk: int):
    """
    Get transport from conf and send code to destination (email/sms)

    """
    otp = otp_sel.get_otp_by_key(pk=pk)
    if otp is not None:
        transport_class = conf.TRANSPORT_CLASS
        with transport_class(otp) as transport:
            transport.send_code()
