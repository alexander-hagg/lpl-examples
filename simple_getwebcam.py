import imageio.v3 as iio
import numpy as np

for idx, frame in enumerate(iio.imiter("<video0>")):
    print(f"Frame {idx}: avg. color {np.sum(frame, axis=-1)}")