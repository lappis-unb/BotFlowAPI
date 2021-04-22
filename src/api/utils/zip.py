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

def create_file_folder(project):
    to_create = os.path.join(tmp_dir, str(project.id))
    
    try:
        os.mkdir(to_create)
    except FileExistsError:
        pass

    return to_create

def create_timestamp():
    delta = timedelta(hours=-3)
    fuso = timezone(delta)
    now = datetime.now().astimezone(fuso)

    return now.strftime('%d-%m-%Y_%H-%M')
    
def get_zipped_files(project, files_dict):
    files_folder = create_file_folder(project)
    
    # Generate and save files into folder
    filenames = save_dict_into_files(files_dict, files_folder)

    zip_filename = "{0}_{1}.zip".format(project.name, create_timestamp())

    zip_path = os.path.join(tmp_dir, zip_filename)

    zip_filenames = {}
    zip_filenames['intents.md'] = 'data/intents/intents.md'
    zip_filenames['stories.md'] = 'data/stories/stories.md'
    zip_filenames['domain.yml'] = 'domain.yml'

    with zipfile.ZipFile(zip_path,'w') as zip: 
        for file in filenames: 
            zip.write(file, zip_filenames[os.path.basename(file)])

    return zip_filename, zip_path

