"""Functions for processing FITS files"""

from astropy import units
from astropy.convolution import convolve
from astropy.io import fits
from django.conf import settings
from radio_beam import Beam

BEAM = 1.5000000363216


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


def load_sub_image_data(filename, y_min, x_min, size):
    """Load in FITS file and create sub section of image data given x,y
    pixel limits"""
    image_data = read_in_fits(filename)
    return create_sub_image(image_data, y_min, x_min, size)


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


def gauss_kernel(beam, pixel_scale):
    """Generate Gaussian kernel of beam size"""
    converted_beam = Beam(beam * units.arcsec)
    return converted_beam.as_kernel(pixel_scale * units.arcsec)


def convolve_image_gaussian(image):
    """Convolve given image with Gaussian kernel"""
    return convolve(image, gauss_kernel(BEAM, settings.PIX_TO_ARCSECONDS))


def clip_image(image, clip_limit):
    """Clip all pixel values in image below zero to zero"""
    image[image < clip_limit] = 0
    return image
