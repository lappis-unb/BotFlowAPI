import zipfile
import os
from io import StringIO
from datetime import datetime, timedelta, timezone

from django.core.files import File

module_dir = os.path.dirname(__file__)
tmp_dir = os.path.join(module_dir, 'tmp')

def save_dict_into_files(files_dict, folder):
    filenames = []
    for key in files_dict:
        new_file = "{0}/{1}".format(folder, key)
        with open(new_file, 'w') as f:
            myfile = File(f)
            myfile.write(files_dict[key])
            filenames.append(new_file)
    return filenames

def get_zipped_files(project, files_dict):
    # Prepare folder to save files
    to_create = os.path.join(tmp_dir, str(project.id))
    
    try:
        os.mkdir(to_create)
    except FileExistsError:
        pass

    files_folder = os.path.join(tmp_dir, str(project.id))
    
    # Generate and save files into folder
    filenames = save_dict_into_files(files_dict, files_folder)

    # Get files and zip
    delta = timedelta(hours=-3)
    fuso = timezone(delta)
    now = datetime.now().astimezone(fuso)
    time_stamp = now.strftime('%d-%m-%Y_%H-%M')

    zip_filename = "{0}_{1}.zip".format(project.name, time_stamp)

    zip_path = os.path.join(tmp_dir, zip_filename)

    with zipfile.ZipFile(zip_path,'w') as zip: 
        for file in filenames: 
            zip.write(file, os.path.basename(file))

    return zip_filename, zip_path

