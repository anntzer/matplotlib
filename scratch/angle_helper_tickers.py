import matplotlib as mpl
from matplotlib import pyplot as plt
from mpl_toolkits.axisartist import floating_axes, angle_helper


vmax = .01

fig = plt.figure()
ax = floating_axes.FloatingSubplot(
    fig, 111,
    grid_helper=floating_axes.GridHelperCurveLinear(
        mpl.transforms.IdentityTransform(), extremes=(0, vmax, 0, vmax),
        grid_locator2=angle_helper.LocatorDMS(10),
        tick_formatter2=angle_helper.FormatterDMS(),
    ),
)
fig.add_axes(ax)

fig, ax = plt.subplots()
ax.set(xlim=(0, vmax), ylim=(0, vmax))
ax.yaxis.set(major_locator=mpl.dates.AutoDateLocator(),
             major_formatter=mpl.ticker.FuncFormatter(lambda x: str(x)))

plt.show()
