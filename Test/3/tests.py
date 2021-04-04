# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:36:11 2021

@author: Flyin
"""
import time
import os
import psutil

class my_tests():
    number_of_tests = 0
    
    def __init__(self, name):
        """Constructor"""
        my_tests.number_of_tests += 1
        self.tc_id = my_tests.number_of_tests
        self.name = name

    def prep(self):
        return "Done"

    def run(self):
        return "Done"
    
    def clean_up(self):
        return "Done"
      
    def execute(self):
        print("Test id",self.tc_id,"named",self.name,"started")
        test_work = True
        try:
            ans = self.prep()
            print("prep :", ans)
            try:
                ans = self.run()
                print("run :", ans)
            except Exception as excep:
                print("run :", excep)
                test_work = False
        except Exception as excep:
            print("prep :", excep)
            test_work = False
        try:
            ans = self.clean_up()
            print("clean_up :", ans)
        except Exception as excep:
            print("clean_up :", excep)
            test_work = False
        if test_work:
            print("Test id",self.tc_id,"named",self.name,"passed")
        else:
            print("Test id",self.tc_id,"named",self.name,"failed")

class my_test_get_files(my_tests):
    
    def __init__(self):
        """Constructor"""
        my_tests.__init__(self,"get_files")
    
    def prep(self):
        t = int(time.time())
        #print(t)
        if t % 2 != 0:
            raise Exception("Time not even")
        return "Done"
            
    def run(self):
        homepath = os.getenv('USERPROFILE')
        print(os.listdir(homepath))
        return "Done"

class my_test_create_file(my_tests):
    
    def __init__(self):
        """Constructor"""
        my_tests.__init__(self,"create_file")
        self.file_name = "file.txt"

    def prep(self):
        t = psutil.virtual_memory()
        #print(t[0])
        if t[0] < 2**30:
            raise Exception("virtual memory less then 1 GB")
        return "Done"
            
    def run(self):
        with open(self.file_name, "w") as out:
            out.truncate(1024 * 1024)       
            out.close()
        return "Done"

    def clean_up(self):
        os.remove(self.file_name)
        return "Done"
    
    
 
if __name__ == "__main__":
    test = my_test_create_file()
    test.execute()
    test = my_test_create_file()
    test.execute()
    test = my_test_get_files()
    test.execute()
        
        
