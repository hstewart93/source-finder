from matplotlib import pyplot as plt

from app.fits_functions import clip_image, convolve_image_gaussian, load_sub_image_data

# Constants
FILENAME = "/Users/bi19158/Code/ska-challenge-1/SKAMid_B1_8h_v3.fits"
Y_MIN = 17500
X_MIN = 16500
SIZE = 500


def plot_convolved_clipped_image(image):
    """Convolve image with Gaussian and clip to zero, then plot image"""
    convolved_image = convolve_image_gaussian(image)
    clipped_image = clip_image(convolved_image, 0)
    plt.imshow(clipped_image)


# Load in and open fits file
# TODO: make this file load dynamic, create a model for fits image and a management command to read it in
sub_image = load_sub_image_data(FILENAME, Y_MIN, X_MIN, SIZE)

plot_convolved_clipped_image(sub_image)
plt.show()
