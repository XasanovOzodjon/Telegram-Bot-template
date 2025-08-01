from . import errors
from .users import start, help, echo
from . import groups
from . import channels

def register_handlers(dp):
    start.register_handlers(dp)
    help.register_handlers(dp)
    echo.register_handlers(dp)
