import matplotlib.pyplot as plt
import numpy as np

def load_points_from_file(file_path):
    # Load points from an .xy file
    points = np.loadtxt(file_path)
    return points

def plot_data(points):
    fig, ax1 = plt.subplots(1, 1, figsize=(12, 6))

    # Plot original points
    ax1.scatter(points[:, 0], points[:, 1], color='blue', label='Point Set')
    ax1.set_title('Original Points')
    ax1.set_aspect('equal')
    ax1.legend()

    plt.tight_layout()
    plt.show()

points = np.loadtxt(r'D:\2D_Denoising\distorted-10.xy')
plot_data(points)