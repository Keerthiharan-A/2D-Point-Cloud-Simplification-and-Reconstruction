import numpy as np
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt

class IdNoise:
    def __init__(self, file_path):
        self.point_set = self.load_xy_data(file_path)

    @staticmethod
    def load_xy_data(file_path):
        """Load point set from a .xy file."""
        return np.loadtxt(file_path)

    def compute_average_distance_and_counts(self):
        """Compute the average distance to closest neighbors and the counts."""
        tree = cKDTree(self.point_set)

        distances, _ = tree.query(self.point_set, k=2)  # k=2 to get the closest neighbor
        closest_distances = distances[:, 1]

        # Calculate the average distance
        average_distance = np.mean(closest_distances) + 2 * np.std(closest_distances)

        # Plot the distances
        self.plot_distances(closest_distances)

        counts = []
        for point in self.point_set:
            count = np.sum(np.linalg.norm(self.point_set - point, axis=1) <= average_distance)
            counts.append(count)

        counts = np.array(counts)

        average_count = np.mean(counts)
        std_dev_count = np.std(counts)

        return average_count, std_dev_count, counts

    @staticmethod
    def plot_distances(closest_distances):
        """Plot the distribution of distances to closest neighbors."""
        plt.figure(figsize=(10, 6))
        plt.hist(closest_distances, bins=30, color='skyblue', edgecolor='black')
        plt.title('Distribution of Distances to Closest Neighbors')
        plt.xlabel('Distance')
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()

    def get_classification(self):
        """Classify the point set as Clean or Noisy based on the average count."""
        average_count, std_dev_count, _ = self.compute_average_distance_and_counts()
        range_value = average_count + 2 * std_dev_count
        return "Clean" if range_value < 3 else "Noisy"

    @staticmethod
    def plot_frequency(counts):
        """Plot the frequency of counts of points within average distance."""
        plt.figure(figsize=(10, 6))
        plt.hist(counts, bins=np.arange(counts.min(), counts.max() + 1) - 0.5,
                 color='skyblue', edgecolor='black')
        plt.title('Frequency Plot of Counts of Points Within Average Distance')
        plt.xlabel('Count of Points')
        plt.ylabel('Frequency')
        plt.grid()
        plt.xticks(np.arange(counts.min(), counts.max() + 1))
        plt.show()

# Example usage
file_path = r'D:\image-data\2D_Dataset\car\BandNoise\car-01-7.5-2.xy'  # Replace with your .xy file path
id_noise = IdNoise(file_path)

average_count, std_dev_count, counts = id_noise.compute_average_distance_and_counts()

print(f"Average count of points in surrounding circle: {average_count:.4f}")
print(f"Standard deviation of counts: {std_dev_count:.4f}")

# Plot the frequency of counts
IdNoise.plot_frequency(counts)

# Check classification
classification = id_noise.get_classification()
print(f"The classification of the point set is: {classification}")