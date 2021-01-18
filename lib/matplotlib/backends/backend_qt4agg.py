"""
Render to qt from agg
"""

from .. import _api
from .backend_qtagg import (
    _BackendQTAgg, FigureCanvasQTAgg, FigureManagerQT, NavigationToolbar2QT)


_api.warn_deprecated("3.3", name=__name__, obj_type="backend")


@_BackendQTAgg.export
class _BackendQT4Agg(_BackendQTAgg):
    pass
