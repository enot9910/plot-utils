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

def calc_buffer(lims, percent_buffer=0.15):
    data_range = lims[1] - lims[0]
    buffer = percent_buffer * data_range
    new_lims = (lims[0] - buffer, lims[1] + buffer)
    return new_lims

def calc_plot_limit(data, percentile=[1, 99.5], percent_buffer=0.3):
    lims = get_data_percentile(data, percentile)
    new_lims = calc_buffer(lims, percent_buffer=percent_buffer)
    return new_lims

def calc_plot_limits(df, feature, target, percentile, percent_buffer=[0.15, 0.15]):
    y_lims = get_data_percentile(df[feature], percentile=percentile)
    x_lims = get_data_percentile(df[target], percentile=percentile)
    x_lims_new = calc_buffer(x_lims, percent_buffer[0])
    y_lims_new = calc_buffer(y_lims, percent_buffer[1])
    return x_lims_new, y_lims_new

def set_plot_limits(xlims, ylims, ax=None):
    if ax is None:
        ax = plt.gca()
    
    if np.isfinite(list(xlims)).all():
        ax.set_xlim(*xlims)
    if np.isfinite(list(ylims)).all():
        ax.set_ylim(*ylims)