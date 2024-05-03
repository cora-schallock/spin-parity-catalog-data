#import external libraries:
import requests
from bs4 import BeautifulSoup

#constants:
BASE_URL = "https://ps1images.stsci.edu/cgi-bin/ps1cutouts?pos={}&filter=color&filter=g&filter=r&filter=i&filter=z&filter=y&filetypes=stack&auxiliary=data&auxiliary=mask&size={}&output_size=256&verbose=0&autoscale=99.500000&catlis0t="
BANDS = ['g','r','i','z','y']
FITS_CUTOUT_LABEL = 'FITS-cutout'

#https://stackoverflow.com/questions/42820342/get-text-in-between-two-h2-headers-using-beautifulsoup

#helper functions:
def _current_band_from_td_element(td_element):
    '''get waveband from image title'''
    current_band = ""
    for each_element in td_element:
        parsed_name = str(each_element).strip().split(" ")[-1]
        if parsed_name in BANDS:
            return parsed_name
    return ""

def _is_fits_cutout(link):
    '''check if link is to FITS-cutout image'''
    return str(link.string) == FITS_CUTOUT_LABEL

def _format_link(link):
    return "http:{}".format(link)

def is_valid_url(url):
    '''check if url is valid'''
    request = requests.get(url)
    return request.status_code == 200

def _is_stack_mask(td_object):
    return "stack.mask" in td_object.get_text()

#functions:
def get_link_to_color_image(soup_object):
    link_to_color_image = ""

    for td in soup_object.findAll("td"):
        for img in td.find_all('img'):
            link_to_color_image = _format_link(img.get("src"))
            break
        break
    return link_to_color_image

def get_ra_dec_string(soup_object):
    ra_dec_string = ""
    
    for each in soup_object.findAll("h2"):
        ra_dec_string = each.get_text(strip=True).strip()
        break
    return ra_dec_string

def get_arcsec_size(soup_object):
    arcsec_size = ""
    
    for each in soup_object.findAll("span"):
        arcsec_size = each.get_text(strip=True).strip()
        break
    return arcsec_size

def get_fits_cutout_links(soup_object):
    wave_band_to_link_dict = {}
    wave_band_to_mask_link_dict = {}
    
    for td in soup_object.findAll("th"):
        current_band = _current_band_from_td_element(td)

        is_mask = _is_stack_mask(td)

        for link in td.find_all('a', href=True):
            #print(link.string)
            if _is_fits_cutout(link) and current_band in BANDS:
                if _is_stack_mask(td):
                    wave_band_to_mask_link_dict.update({current_band:_format_link(link['href'])})
                else:
                    wave_band_to_link_dict.update({current_band:_format_link(link['href'])})
    return (wave_band_to_link_dict,wave_band_to_mask_link_dict)
        
def retrieve_info_for_galaxy(galaxy_name,pixel_size=240):
    url = ""
    color_image_link = ""
    ra_dec_string = ""
    arcsec_size_string = ""
    fits_cutout_link_dict = {}
    fits_cutout_mask_link_dict = {}
    
    try:
        #url = BASE_URL.format(galaxy_name,pixel_size)
        gal_name = galaxy_name.replace(' ','+') #to take care of space in name
        gal_name = gal_name.replace('+','%2B') #for + sign i.e. IRAS03056+2034
        url = BASE_URL.format(gal_name,pixel_size)
        
        if is_valid_url(url):
            
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")

            color_image_link = get_link_to_color_image(soup)
            (fits_cutout_link_dict,fits_cutout_mask_link_dict) = get_fits_cutout_links(soup)

            ra_dec_string = get_ra_dec_string(soup)
            arcsec_size_string = get_arcsec_size(soup)
        else:
            print("invalid url: {}".format(url))
    except Exception as e:
        print("error in function get_all_fits_cutout_links_for_band: {}".format(e))

    return (url, ra_dec_string, arcsec_size_string, color_image_link, fits_cutout_link_dict, fits_cutout_mask_link_dict)
