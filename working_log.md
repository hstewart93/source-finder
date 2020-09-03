# Working Log of Software

## Data
The data is collected from the official SKA [website](https://astronomers.skatelescope.org/ska-science-data-challenge-1/). The first data challenge has 9 images in
total, 3 different frequencies at 3 observing times. This is source data that I will be attempting to detect and classify simple and complex sources within. There
is also a truth catalogue for each channel with all sources present labelled with information such as pixel centers (x, y), semi-major and semi-minor axes, position
angle and class.

The classes are given as:
* 1 for SS-AGNs
* 2 for FS-AGNs
* 3 for SFGs (Star forming galaxies)

## Postgres Database and Django ORM
### Building TrueSource model
I built the TrueSource model based on the information provided in the header of the truth catalogue. For each field present in the table I created a model field for
this information. The benefit of creating a model to represent this data is that once it has been created as an object in the database, the data will follow a conventions
laid out by myself and by the Django model. This means the data will behave as expected and more importantly without change every time I query the database. Any issues
with data cleanliness can be dealt with as it is imported into the database. An object can then be easily queried and updated using the Djano ORM.

### Loading Truth labels
I have written a management command to load the data into the database which can be found at `sources/management/commands/import_truth_file.py`. It works by iterating
through every line in the txt file given and subsequently creating a TrueSource object for that line. This was initially written in series and took over 10 minutes to
created the ~30_000 objects. However, using the `map` function I rewrote the command in parallel and it now creates these objects in under 1 minute. It can be easily
paralellised as each object is independent and can be created alongside other objects in the list.

## Multi-classifier CNN
### Implementing animal classification tutorial

Using this [repository](https://github.com/imamun93/animal-image-classifications) and following the `final_notebook.ipnb` within it I built a multi-classifier CNN
that can classify a single animal within an image from a set of given labels. It might be a useful avenue to pursue to apply this method to my own source data.

### Building training set of source data
To use the multi-classifier CNN above, the data needs to be cut into sub images that are cut around a true source whose information can be collected from the truth
label set. These images will need to be separated into directories labelled by their classification and then the CNN can be trained. Since the true labels are now
in the database as TrueSource objects I can easily extract labels for a given sub-section of the data. In this experiment I will be using a densely populated area
of the image from the *560 MHz channel at 8 hours observing time*. The coordinates of the bottom left corner of the sub-section are `x, y = 16_500, 17_000`. The
sub-section is size `500 x 500` pixels.
