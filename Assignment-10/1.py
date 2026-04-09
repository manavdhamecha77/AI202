import random
import matplotlib.pyplot as plt


# Load CSV 
def load_data(filename):
    points = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            x = float(parts[0])
            y = float(parts[1])
            points.append([x, y])
    return points

points = load_data("Assignment-10/cities.csv")


# Distance squared
def dist2(p, c):
    return (p[0] - c[0])**2 + (p[1] - c[1])**2

# Convergence function
def has_converged(old, new, tol=0.000123):
    for i in range(len(old)):
        dx = old[i][0] - new[i][0]
        dy = old[i][1] - new[i][1]
        if dx*dx + dy*dy > tol:
            return False
    return True


# SSD
def compute_ssd(points, centroids):
    total = 0
    for p in points:
        min_d = float('inf')
        for c in centroids:
            d = dist2(p, c)
            if d < min_d:
                min_d = d
        total += min_d
    return total


# Assign clusters
def assign_clusters(points, centroids):
    clusters = [[] for i in range(len(centroids))]

    for p in points:
        best_idx = 0
        best_dist = dist2(p, centroids[0])

        for i in range(1, len(centroids)):
            d = dist2(p, centroids[i])
            if d < best_dist:
                best_dist = d
                best_idx = i

        clusters[best_idx].append(p)

    return clusters


# Mean of points
def mean(points):
    if not points:
        return [0, 0]

    x_sum = 0
    y_sum = 0

    for p in points:
        x_sum += p[0]
        y_sum += p[1]

    return [x_sum / len(points), y_sum / len(points)]


# Gradient Descent
def gradient_descent(points, k=3, lr=0.123, max_epochs=99):
    centroids = random.sample(points, k)

    for epoch in range(max_epochs):
        old_centroids = [c[:] for c in centroids]

        clusters = assign_clusters(points, centroids)

        for i in range(k):
            if clusters[i]:
                m = mean(clusters[i])
                centroids[i][0] -= lr * (centroids[i][0] - m[0])
                centroids[i][1] -= lr * (centroids[i][1] - m[1])

        if has_converged(old_centroids, centroids):
            return centroids, epoch + 1

    return centroids, max_epochs

# Newton Method
def newton_method(points, k=3, max_epochs=99):
    centroids = random.sample(points, k)

    for epoch in range(max_epochs):
        old_centroids = [c[:] for c in centroids]

        clusters = assign_clusters(points, centroids)

        for i in range(k):
            if clusters[i]:
                centroids[i] = mean(clusters[i])

        if has_converged(old_centroids, centroids):
            return centroids, epoch + 1

    return centroids, max_epochs

# Run both methods
gd_centroids, gd_iter = gradient_descent(points)
nr_centroids, nr_iter = newton_method(points)

gd_ssd = compute_ssd(points, gd_centroids)
nr_ssd = compute_ssd(points, nr_centroids)

print("Gradient Descent SSD:", gd_ssd)
print("Iterations:", gd_iter)

print("\nNewton Method SSD:", nr_ssd)
print("Iterations:", nr_iter)

# Plots
x = [p[0] for p in points]
y = [p[1] for p in points]

plt.figure()

plt.subplot(1, 2, 1)  

plt.scatter(x, y)

for c in gd_centroids:
    plt.scatter(c[0], c[1], marker='X', s=200)

plt.title("Gradient Descent")
plt.xlabel("A")
plt.ylabel("B")

plt.subplot(1, 2, 2)

plt.scatter(x, y)

for c in nr_centroids:
    plt.scatter(c[0], c[1], marker='X', s=200)

plt.title("Newton Method")
plt.xlabel("A")
plt.ylabel("B")

plt.show()