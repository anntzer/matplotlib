from .backend_qt import (
    backend_version, SPECIAL_KEYS,
    SUPER, ALT, CTRL, SHIFT, MODIFIER_KEYS,  # These are deprecated.
    cursord, _create_qApp, _BackendQT, TimerQT, MainWindow, FigureCanvasQT,
    FigureManagerQT, NavigationToolbar2QT, SubplotToolQt)


@_BackendQT.export
class _BackendQT5(_BackendQT):
    pass
