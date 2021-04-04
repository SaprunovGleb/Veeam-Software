# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 11:00:55 2021

@author: Flyinmark
"""

import xml.etree.ElementTree as ET
import os
import shutil
import sys


def copy_files_using_sorce_xml(xml_file="files.xml"):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for elem in root:
        source_path=elem.attrib['source_path']
        if source_path[0] == '/' or source_path[0] == '\\':
            source_path = os.getcwd() + source_path
        file_name = elem.attrib['file_name']
        file_path = source_path + '\\' + file_name
        if not os.path.isfile(file_path):
            print('file named ',file_name,' in dir ', source_path, ' is NOT exist') 
        else:
            destination_path = elem.attrib['destination_path']
            if destination_path[0] == '/' or destination_path[0] == "\\":
                destination_path = os.getcwd() + destination_path
            if not os.path.isdir(destination_path):
                os.makedirs(destination_path)
            try:
                shutil.copy(file_path, destination_path)
                print('file named',file_name,'from dir', source_path, 'is copyed to', destination_path)
            except Exception as excep:
                print('file named',file_name,'from dir', source_path, 'can not be copyed to', 
                      destination_path, 'Exception:', excep)
        print('\n')
        
if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        copy_files_using_sorce_xml(args[1])
    else:
        copy_files_using_sorce_xml()