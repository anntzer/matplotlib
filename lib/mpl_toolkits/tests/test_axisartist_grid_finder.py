# This whole test module can go away once mpl_toolkits tickers are gone.


import matplotlib as mpl
from mpl_toolkits.axisartist.grid_finder import (
    FormatterPrettyPrint, MaxNLocator)


def test_pretty_print_format():
    locator = MaxNLocator()
    locs, nloc, factor = locator(0, 100)
    fmt = FormatterPrettyPrint()
    assert fmt("left", None, locs) == \
        [r'$\mathdefault{%d}$' % (l, ) for l in locs]


def test_pretty_print_format_mpl_api():
    loc = mpl.ticker.MaxNLocator()
    fmt = mpl.ticker.ScalarFormatter(useMathText=True, useOffset=False)
    fmt.create_dummy_axis()
    locs = loc.tick_values(0, 100)
    assert fmt.format_ticks(locs) == [r'$\mathdefault{%d}$' % l for l in locs]
