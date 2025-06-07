import numpy as np
import matplotlib.pyplot as plt 

def get_data_percentile(data, percentile=[1, 99.5]):
    clean_data = np.array(data)
    clean_data = clean_data[~np.isnan(clean_data)]
    clean_data = clean_data[np.isfinite(clean_data)]

    if len(clean_data) == 0:
        return np.nan, np.nan
    
    p_low, p_high = np.percentile(data, percentile)
    return p_low, p_high

def calc_buffer(xlims, ylims, percent_buffer=0.15):
    x_buffer = percent_buffer * (xlims[1] - xlims[0])
    y_buffer = percent_buffer * (ylims[1] - ylims[0])

    x_new = (xlims[0] - x_buffer, xlims[1] + x_buffer)
    y_new = (ylims[0] - y_buffer, ylims[1] + y_buffer)

    return x_new, y_new

def calc_plot_limits(df, feature, target, percentile, percent_buffer):
    y_lims = get_data_percentile(df[feature], percentile=percentile)
    x_lims = get_data_percentile(df[target], percentile=percentile)
    return calc_buffer(x_lims, y_lims, percent_buffer)

def set_plot_limits(xlims, ylims, ax=None):
    if ax is None:
        ax = plt.gca()
    
    if np.isfinite(list(xlims)).all():
        ax.set_xlim(*xlims)
    if np.isfinite(list(ylims)).all():
        ax.set_ylim(*ylims)