import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import make_lupton_rgb
from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
import os
from PIL import Image

TABLE_NAME = 'figure11'

def construct_color_fits(name):
    g_path = "/mnt/c/Users/school/Desktop/github/spin-parity-catalog-data/sdss/{}/{}/{}_g.fits".format(TABLE_NAME,name,name)
    r_path = "/mnt/c/Users/school/Desktop/github/spin-parity-catalog-data/sdss/{}/{}/{}_r.fits".format(TABLE_NAME,name,name)
    i_path = "/mnt/c/Users/school/Desktop/github/spin-parity-catalog-data/sdss/{}/{}/{}_i.fits".format(TABLE_NAME,name,name)
    save_path = "/mnt/c/Users/school/Desktop/github/spin-parity-catalog-data/sdss/{}/{}/{}_color.png".format(TABLE_NAME,name,name)

    if not os.path.exists(g_path) or not os.path.exists(r_path) or not os.path.exists(i_path): return

    g = fits.open(g_path)[0].data
    r = fits.open(r_path)[0].data*0.8
    i = fits.open(i_path)[0].data*0.7

    rgb = make_lupton_rgb(i, r, g, Q=10, stretch=0.3, minimum=0.0)
    pil_img = Image.fromarray(rgb)
    pil_img.save(save_path)

def run():
    for name in os.listdir("/mnt/c/Users/school/Desktop/github/spin-parity-catalog-data/sdss/{}".format(TABLE_NAME)):
        print(name)
        construct_color_fits(name)

if __name__ == "__main__":
    run()
