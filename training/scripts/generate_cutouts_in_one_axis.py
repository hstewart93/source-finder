"""Import FITS image data and generate 500 x 500 pixel square cut outs
in one axis."""

from matplotlib import pyplot as plt
import numpy as np

from app.fits_functions import load_sub_image_data, read_in_fits

# Constants
FILENAME = "/Users/bi19158/Code/ska-challenge-1/SKAMid_B1_8h_v3.fits"
Y = 20_000
SIZE = 500

fits_image = read_in_fits(FILENAME)

image = fits_image.data
len_x = fits_image.header["NAXIS2"]

x = np.arange(0, len_x, SIZE)

for i in x:
    data_subset = load_sub_image_data(FILENAME, Y, i, SIZE)
    plt.imshow(data_subset)
    plt.savefig(f"training/data/y_20_000/x_start_{i}.png")
