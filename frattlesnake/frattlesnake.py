from typing import Optional
from html import escape

from .kolmafia import km


def init():
    km.KoLmafia.main(["--GUI"])


def login(username: str, password: Optional[str] = None):
    if password is None:
        password = km.KoLmafia.getSaveState(username)

    request = km.LoginRequest(username, password)
    request.run()
    return request


def abort(message: str = None):
    km.KoLmafia.updateDisplay(km.KoLConstants.MafiaState.ABORT, message)


def log(message: str = "", html: bool = False):
    message = str(message)
    if html is False:
        message = escape(message)

    km.RequestLogger.printLine(message)