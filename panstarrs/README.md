# Pan-STARRS 1: 
## Data:
The FITS images, color composite images, as well as link to the galaxy on the PANSTARRS-1 Image CUtout Service, RA/DEC, and size can be found in the data folders below:

| Figure     |
|------------|
| [Figure #8](https://github.com/cora-schallock/spin-parity-catalog-data/tree/main/panstarrs/figure8)  | 
| [Figure #9](https://github.com/cora-schallock/spin-parity-catalog-data/tree/main/panstarrs/figure9)  | 
| [Figure #10](https://github.com/cora-schallock/spin-parity-catalog-data/tree/main/panstarrs/figure10) | 
| [Figure #11](https://github.com/cora-schallock/spin-parity-catalog-data/tree/main/panstarrs/figure11) | 

## Missing Galaxies:
Below is a table indicating the number of galaxies in each figure from Spin Parity paper and the number of galaxies that are present in this catalog:

| Figure     | Spin Parity Paper Count | Spin Parity Catalog Count |
|------------|-------|---------------------------|
| Figure #8  | 146   | 135                       |
| Figure #9  | 321   | 303                       |
| Figure #10 | 63    | 62                        |
| Figure #11 | 25    | 25                        |

Figure #8 Missing Galaxies:
- Circinus Galaxy: missing from survey
- NGC224: doesn't match one in paper
- NGC247: bottom of disk cut off
- NGC253: has many streaks across the image
- NGC598: missing (too large of a file for github)
- NGC1386: missing from survey (in ESSO)
- NGC1532: missing from survey (in ESSO)
- NGC1566: missing from survey (in ESSO)
- NGC3031: missing from survey (in ESSO)
- NGC4622: missing from survey

Figure #9 Missing Galaxies:
- NGC300: missing from survey (in ESSO)
- NGC1512: missing
- NGC2915: missing from survey (in ESSO)
- NGC2997: has many streaks
  
Figure #10 Missing Galaxies:
- NGC3621: missing from survey (in ESSO)

## Downloader:
The [downloader folder](https://github.com/cora-schallock/spin-parity-catalog-data/tree/main/panstarrs/downloader-scripts) contains scripts you can run to download your own copy of the data from the PANSTARRS Image Cutout Service.

## Cutoutsize:
The [cutout size folder](https://github.com/cora-schallock/spin-parity-catalog-data/tree/main/panstarrs/cutout_size) contains the image cutout size parameter used for each galaxy in the catalog [in units of pixels]. Please note that for this survery the conversion between that and arcseconds is 1 pixel = 0.25 arcsec. The size information for each downloaded galaxy can also be found in the "size text file" (for example for NGC1 it is called [NGC1_size.txt](https://github.com/cora-schallock/spin-parity-catalog-data/blob/main/panstarrs/figure9/NGC1/NGC1_size.txt)).

