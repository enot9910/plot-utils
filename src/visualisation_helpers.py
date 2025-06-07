import numpy as np

def add_shake(y_values, delta, threshold=200, shake_pct=0.25):
    y_values_shaked = y_values.copy()
    
    if len(np.unique(y_values)) < threshold:
        shake_delta = delta * (shake_pct / 100)
        y_values_shaked += np.random.uniform(
            -shake_delta, shake_delta, size=len(y_values)
        )
    return y_values_shaked