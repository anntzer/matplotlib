from .. import _api
from .backend_qtcairo import _BackendQTCairo, FigureCanvasQTCairo


_api.warn_deprecated("3.3", name=__name__, obj_type="backend")


@_BackendQTCairo.export
class _BackendQT4Cairo(_BackendQTCairo):
    pass
