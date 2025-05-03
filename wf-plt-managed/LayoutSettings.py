
class LayoutSettings:
    def __init__(self, nrows, ncols,
                 subplot_width_in=3.0,
                 subplot_height_in=2.5,
                 spacing_in=0.5,
                 margin_in=0.75,
                 colorbar_width_in=0.3):
        self.nrows = nrows
        self.ncols = ncols
        self.subplot_width_in = subplot_width_in
        self.subplot_height_in = subplot_height_in
        self.spacing_in = spacing_in
        self.margin_in_left = margin_in[0]
        self.margin_in_up = margin_in[1]
        self.margin_in_right = margin_in[2]
        self.margin_in_down = margin_in[3]
        self.colorbar_width_in = colorbar_width_in

        self.figsize = self.calculate_figsize()

    def calculate_figsize(self):
        width = (self.ncols * self.subplot_width_in) + ((self.ncols - 1) * self.spacing_in) + (self.margin_in_left + self.margin_in_right)
        height = (self.nrows * self.subplot_height_in) + ((self.nrows - 1) * self.spacing_in) + (self.margin_in_down + self.margin_in_up)
        return (width, height)

    def get_subplot_position(self, row, col):
        fig_w, fig_h = self.figsize

        left_in = self.margin_in_left + col * (self.subplot_width_in + self.spacing_in)
        bottom_in = self.margin_in_up + (self.nrows - 1 - row) * (self.subplot_height_in + self.spacing_in)

        left = left_in / fig_w
        bottom = bottom_in / fig_h
        width = self.subplot_width_in / fig_w
        height = self.subplot_height_in / fig_h

        return [left, bottom, width, height]
