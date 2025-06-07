import numpy as np

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

    x_min = xlims[0] - x_buffer
    x_max = xlims[1] + x_buffer
    y_min = ylims[0] - y_buffer
    y_max = ylims[1] + y_buffer

    return x_min, x_max, y_min, y_max

def calc_plot_limits(df, feature, target, percentile, percent_buffer):
    y_lims = get_data_percentile(df[feature], percentile=percentile)
    x_lims = get_data_percentile(df[target], percentile=percentile)
    return calc_buffer(x_lims, y_lims, percent_buffer)