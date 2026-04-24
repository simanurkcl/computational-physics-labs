import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# -------------------------
# Experimental Data
# -------------------------

# Acrylic
theta1_acrylic = np.array([15, 22, 30, 35, 45])
theta2_acrylic = np.array([12.5, 22.5, 27.5, 35, 40])

# Water
theta1_water = np.array([10, 25, 35, 45, 53])
theta2_water = np.array([6.5, 18.5, 25, 32.5, 36.5])

# Glycerin
theta1_glycerin = np.array([10, 25, 35, 45, 53])
theta2_glycerin = np.array([8.5, 19.5, 23.5, 34, 38.5])

# -------------------------
# Snell Law Function
# n1 sin(theta1) = n2 sin(theta2)
# Assume n1 = air ≈ 1
# so n ≈ sin(theta1)/sin(theta2)
# -------------------------

def compute_n(theta1, theta2):
    return np.sin(np.radians(theta1)) / np.sin(np.radians(theta2))

# Compute refractive indices
n_acrylic = compute_n(theta1_acrylic, theta2_acrylic)
n_water = compute_n(theta1_water, theta2_water)
n_glycerin = compute_n(theta1_glycerin, theta2_glycerin)

# Averages
materials = ["Acrylic", "Water", "Glycerin"]
means = [np.mean(n_acrylic), np.mean(n_water), np.mean(n_glycerin)]

# -------------------------
# Plot 1: Refractive indices
# -------------------------
plt.figure()

plt.bar(materials, means)
plt.ylabel("Refractive Index")
plt.title("Measured Refractive Indices")

plt.savefig("../plots/refractive_indices.png")
plt.show()

# -------------------------
# Plot 2: Snell law linear fit
# sin(theta1) vs sin(theta2)
# -------------------------

def snell_fit(theta1, theta2, name):
    x = np.sin(np.radians(theta1))
    y = np.sin(np.radians(theta2))

    slope, intercept, r, p, err = linregress(x, y)

    plt.figure()
    plt.scatter(x, y, label="Data")
    plt.plot(x, slope*x + intercept, label=f"Fit: slope={slope:.2f}")

    plt.xlabel("sin(theta1)")
    plt.ylabel("sin(theta2)")
    plt.title(f"Snell's Law Verification - {name}")
    plt.legend()

    plt.savefig(f"../plots/snell_fit_{name}.png")
    plt.show()

    return slope

snell_fit(theta1_acrylic, theta2_acrylic, "acrylic")
snell_fit(theta1_water, theta2_water, "water")
snell_fit(theta1_glycerin, theta2_glycerin, "glycerin")
