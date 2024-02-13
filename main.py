import os
from PIL import Image
import json
import shutil

def process_folder(folder_path):
    # get a list of all the files and folders in the current directory
    files_and_folders = os.listdir(folder_path)

    # initialize a dictionary to store JPEG and JSON file pairs
    file_pairs = {}

    