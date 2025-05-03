import matplotlib.pyplot as plt

from SubplotManager import SubplotManager
from LayoutSettings import LayoutSettings

class PlotManager:
    def __init__(self, layout, **kwargs):
        self.layout = layout
        self.fig = None

    def __enter__(self):
        self.fig = plt.figure(figsize=self.layout.figsize)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
        
    def subplot(self, row, col, with_colorbar=False, title=None, xlabel=None, ylabel=None):
        pos = self.layout.get_subplot_position(row, col)
        ax = self.fig.add_axes(pos)
        return SubplotManager(ax,
                              with_colorbar=with_colorbar,
                              colorbar_width=self.layout.colorbar_width_in / self.layout.figsize[0],
                              title=title,
                              xlabel=xlabel,
                              ylabel=ylabel)
