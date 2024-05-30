import subprocess
import csv

#/mnt/c/Users/school/Downloads/SDSS_fits_cutout/get_sdss_a
#tlas.sh 0.33237 34.52572 0.025 IC5376_test

PATH_TO_SCRIPT = '/mnt/c/Users/school/Downloads/SDSS_fits_cutout/get_sdss_atlas.sh'

def get_mosaic_info_from_csv(csv_path):
    the_rows = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['name']
            ra = row['ra']
            dec = row['dec']
            the_size = row['size_deg']

            if ' ' in name:
                name = name.replace(' ','')
            the_rows.append([name,ra,dec,the_size])
    return the_rows

def run_mosaic_creation_on_rows(rows):
    i = 1
    for row in rows:
        if len(row) != 4: continue
        
        name = row[0]
        ra = row[1]
        dec = row[2]
        the_size = row[3]

        print("running on {} of {}: {}".format(i,len(rows),name))
        subprocess.call(['sh', PATH_TO_SCRIPT,ra,dec,the_size,name])
        i+=1

if __name__ == "__main__":
    csv_path = 'figure11.csv'
    
    the_rows = get_mosaic_info_from_csv(csv_path)
    run_mosaic_creation_on_rows(the_rows)
