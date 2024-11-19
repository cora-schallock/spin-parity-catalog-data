import os
import shutil

path_to_input = "/mnt/c/Users/school/Desktop/cross_id/sdss_mosaic_construction"
path_to_output = "/home/cora/SDSS/G.in"

def copy_fits_for_g_in(folder_name):
    for gal_name in os.listdir(os.path.join(path_to_input,folder_name)):
        for file_name in os.listdir(os.path.join(path_to_input,folder_name,gal_name)):
            if "fits" not in file_name: continue

            original_path = os.path.join(path_to_input,folder_name,gal_name,file_name)
            new_path = os.path.join(path_to_output,file_name)
            shutil.copyfile(original_path, new_path)


if __name__ == "__main__":
    copy_fits_for_g_in("figure9")
    #check spaces
