from matplotlib import pyplot as plt

from visualisation.fits_functions import read_in_fits, create_sub_image
from visualisation.true_source_functions import get_subset, surface_brightness_for_set

# Constants
FILENAME = "/Users/bi19158/Code/ska-challenge-1/SKAMid_B1_8h_v3.fits"
Y_MIN = 17500
X_MIN = 16500
SIZE = 500

# Load in and open fits file
# TODO: make this file load dynamic, create a model for fits image and a management command to read it in
image_data = read_in_fits(FILENAME)

sub_image = create_sub_image(image_data, Y_MIN, X_MIN, SIZE)

# Get TrueSource set filtered by pixels limits in sub image
source_set = get_subset(Y_MIN, X_MIN, SIZE)

# Calculate surface brightness for set and order by surface brightness ascending
sorted_set = surface_brightness_for_set(source_set).order_by("-surface_brightness")

y_values = [source.y_centroid - Y_MIN for source in source_set]
x_values = [source.x_centroid - X_MIN for source in source_set]

plt.scatter(y_values[:100], x_values[:100], marker="x")
plt.imshow(sub_image)
plt.show()
