from pathlib import Path
import matplotlib.pyplot as plt

def save_plot(save_path=None, show=True):
    if save_path:
        save_dir = Path(save_path).parent
        save_dir.mkdir(parents=True, exist_ok=True)
        plt.savefig(save_path)
    if show:
        plt.show()
    plt.close()