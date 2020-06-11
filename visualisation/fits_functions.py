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


#
# def clip_image():
#     from astropy.convolution import convolve
#     from astropy import units as u
#     from radio_beam import Beam
#
#     nan_array = np.isnan(image_data)
#
#     if True in nan_array:
#         print("True")
#     else:
#         print("False")
#
#     fits_header = fits.getheader(filename)
#     my_beam = Beam.from_fits_header(fits_header)
#     beam = Beam(1.5000000363216 * u.arcsec)
#
#     pix_scale = 0.6 * u.arcsec
#
#     sub_image = image_data[0, 0, 17500:18000, 16500:17000]
#     # sub_image = image_data[0, 0, 15000:15500, 15000:15500]
#
#     gauss_kernel = beam.as_kernel(pix_scale)
#     image_convolved = convolve(sub_image, gauss_kernel)


def gauss_kernel(beam, pixel_scale):
    """"""
    converted_beam = Beam(beam * units.arcsec)
    return converted_beam.as_kernel(pixel_scale * units.arcsec)


def convolve_image(image):
    """"""
    return convolve(image, gauss_kernel(BEAM, settings.PIX_TO_ARCSECONDS))


def clip_image(image, clip_limit):
    """"""
    image[image < clip_limit] = 0
    return image
