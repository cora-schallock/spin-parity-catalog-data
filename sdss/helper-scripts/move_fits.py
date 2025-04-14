import shutil
import os

TABLE_NAME = 'figure9'
OLD_LOCATION = 'C:\\Users\\school\\Desktop\\cross_id\\sdss_mosaic_construction\\raw'
NEW_LOCATION = 'C:\\Users\\school\\Desktop\\cross_id\\sdss_mosaic_construction'
BANDS = ['u','g','i','r','z']

def get_old_file_path(name,band):
    return os.path.join(OLD_LOCATION,TABLE_NAME,name,band,"{}.fits".format(band))

def get_new_file_path(name,band):
    return os.path.join(NEW_LOCATION,TABLE_NAME,name,"{}_{}.fits".format(name,band))

def move_files():
    table_path = os.path.join(NEW_LOCATION,TABLE_NAME)
    if not os.path.exists(table_path): os.makedirs(table_path)
    
    for gal_name in os.listdir(os.path.join(OLD_LOCATION,TABLE_NAME)):
        for band in BANDS:
            if not os.path.exists(get_old_file_path(gal_name,band)): continue

            folder_path = os.path.join(NEW_LOCATION,TABLE_NAME,gal_name)
            if not os.path.exists(folder_path): os.makedirs(folder_path)

            shutil.copyfile(get_old_file_path(gal_name,band), get_new_file_path(gal_name,band))

if __name__ == "__main__":
    move_files()
