"""Functions for processing FITS files"""

from astropy.io import fits


def read_in_fits(filename):
    """Reads in a FITS file and returns an array"""
    hdul = fits.open(filename)["PRIMARY"]
    return hdul.data


def create_sub_image(image, y_min, x_min, size):
    """Create a square sub image given starting x and y pixel coordinates
    and the size of the square"""
    if len(image.shape) > 2:
        return image[0, 0, y_min : y_min + size, x_min : x_min + size]
    else:
        return image[y_min : y_min + size, x_min : x_min + size]


def create_image_cut_around_source(image, y_center, x_center, size):
    """Function to create a sub image of an image around the center
    of a source for a given size"""
    if len(image.shape) > 2:
        return image[
            0,
            0,
            int(y_center - size) : int(y_center + size),
            int(x_center - size) : int(x_center + size),
        ]
    else:
        return image[
            int(y_center - size) : int(y_center + size),
            int(x_center - size) : int(x_center + size),
        ]
