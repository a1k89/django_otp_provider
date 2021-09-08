class BaseTransport:
    def __init__(self, otp):
        self.otp = otp

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.otp = None

    def send_code(self):
        raise NotImplemented
