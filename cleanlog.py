import os
import shutil
import sys


if(len(sys.argv) < 4):
    print("[-] Missing aruments!")
    print('Usage: python cleanlog.py your_log.txt 4 10')
    exit(1)
    
file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_number = int(sys.argv[3])

if(os.path.isfile(file_name) == True):
    log_file_size  = os.stat(file_name).st_size / 1024 # in KB

    if(log_file_size >= limit_size):
        if(logs_number > 0):
            for current_file_number in range(logs_number, 1, -1):
                src_file = file_name + '_' + str(current_file_number-1)
                dest_file = file_name + '_' + str(current_file_number)
                if(os.path.isfile(src_file) == True):
                     shutil.copyfile(src_file, dest_file)
                     print('Copied: ' + src_file + ' to ' + dest_file)
            shutil.copyfile(file_name, file_name + '_1')
            print('Copied: ' + file_name + ' to ' + file_name+ '_1')
    
        my_file = open(file_name, 'w') # clear file
        my_file.close()            
    
