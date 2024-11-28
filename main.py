import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
import random

# Parameters for canvas
width, height = 2048, 2048
fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_facecolor((1, 1, 1))  # white background
ax.axis('off')

# Parameters for waves
colors = [(0.5, 0.5, 1), (0, 1, 0.5)]
num_waves = 32


# Function to generate a sine wave
def generate_sine_wave(x, amplitude, frequency, phase_shift, vertical_shift, color, transparency):
    y = amplitude * np.sin(frequency * x + phase_shift) + vertical_shift
    rgba_color = to_rgba(color, transparency)
    return x, y, rgba_color


# Generate sine waves
x = np.linspace(0, width, width)
for _ in range(num_waves):
    amplitude = random.randint(32, 512)
    frequency = random.uniform(0.005, 0.01)
    phase_shift = random.uniform(0, 2 * np.pi)
    padding = 256
    vertical_shift = random.randint(padding, 2048-padding)
    color = random.choice(colors)
    thickness = random.uniform(20,100)
    transparency = random.uniform(0.2, 1-thickness/100)

    x_wave, y_wave, rgba_color = generate_sine_wave(x, amplitude, frequency, phase_shift, vertical_shift, color,
                                                    transparency)

    ax.plot(x_wave, y_wave, color=rgba_color, lw=thickness)

# Save the image
plt.tight_layout()
plt.savefig('waves.png', bbox_inches='tight', pad_inches=0, transparent=False)

# Close the plot to free up memory
plt.close()
