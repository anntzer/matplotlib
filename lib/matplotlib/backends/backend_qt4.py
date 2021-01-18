from .. import _api
from .backend_qt import (
    backend_version, SPECIAL_KEYS,
    SUPER, ALT, CTRL, SHIFT, MODIFIER_KEYS,  # These are deprecated.
    cursord, _create_qApp, _BackendQT, TimerQT, MainWindow, FigureCanvasQT,
    FigureManagerQT, NavigationToolbar2QT, SubplotToolQt)


_api.warn_deprecated("3.3", name=__name__, obj_type="backend")


@_BackendQT.export
class _BackendQT4(_BackendQT):
    pass
