import numpy as np

def get_data_percentile(data, percentile=[1, 99.5]):
    p_low, p_high = np.percentile(data, percentile)
    return p_low, p_high

def get_buffer(xlims, ylims, percent_buffer=0.15):
    x_buffer = percent_buffer * (xlims[1] - xlims[0])
    y_buffer = percent_buffer * (ylims[1] - ylims[0])

    x_min = xlims[0] - x_buffer
    x_max = xlims[1] + x_buffer
    y_min = ylims[0] - y_buffer
    y_max = ylims[1] + y_buffer

    return x_min, x_max, y_min, y_max