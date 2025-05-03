

class SubplotManager:
    def __init__(self, ax, with_colorbar=False, colorbar_width=0.05,
                 title=None, xlabel=None, ylabel=None):
        self.ax = ax
        self.with_colorbar = with_colorbar
        self.colorbar_width = colorbar_width
        self._title = title
        self._xlabel = xlabel
        self._ylabel = ylabel
        self.img = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._title:
            self.ax.set_title(self._title)
        if self._xlabel:
            self.ax.set_xlabel(self._xlabel)
        if self._ylabel:
            self.ax.set_ylabel(self._ylabel)
        if self.with_colorbar and self.img is not None:
            self.add_colorbar(self.img)

    def imshow(self, data, **kwargs):
        """Plot an image and return the image object."""
        img = self.ax.imshow(data, **kwargs)
        return img

    def plot(self, *args, **kwargs):
        """Standard line plot."""
        self.ax.plot(*args, **kwargs)

    def add_colorbar(self, mappable):
        bbox = self.ax.get_position()
        fig = self.ax.figure
        cax_left = bbox.x1 + 0.01
        cax_bottom = bbox.y0
        cax_width = self.colorbar_width
        cax_height = bbox.height
        cax = fig.add_axes([cax_left, cax_bottom, cax_width, cax_height])
        fig.colorbar(mappable, cax=cax)

    def add_legend(self):
        self.ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
