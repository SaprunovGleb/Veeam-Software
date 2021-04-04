# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:58:52 2021

@author: Flyin
"""

import hashlib
import sys
import os
#print(hashlib.algorithms_guaranteed)

def hash_from_file(path_to_input_file, path_to_dir, BUF_SIZE = 65536):
    file_data = open(path_to_input_file, 'r')
    for line in file_data:
        if line[-1] == '\n':
            line = line[:-1]
        listLine = line.split(" ")
        file_path = path_to_dir +'\\'+listLine[0]
        #print (listLine)
        if not os.path.isfile(file_path):
            print(listLine[0],'NOT FOUND')
        else:
            file_to_hach = open(file_path, 'rb')
            if listLine[1] == 'md5':
                m = hashlib.md5()
            if listLine[1] == 'sha1':
                m = hashlib.sha1()
            if listLine[1] == 'sha256':
                m = hashlib.sha256()
            while True:
                buf = file_to_hach.read(BUF_SIZE)
                if not buf:
                    break
                m.update( buf )
            if m.hexdigest() == listLine[2]:
                print(listLine[0],'OK')
            else:
                print(listLine[0],'FAIL')


if __name__ == "__main__":
    args = sys.argv
    hash_from_file(args[1],args[2])
    