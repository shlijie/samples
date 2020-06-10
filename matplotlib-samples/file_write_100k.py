# coding:utf-8
import os
import time

# author:Tammy Pi
# email:victory_pj@163.com
# compare the generate time of 102400 1KB minifile and 100MB big file
filenums = 102400
mini_filepath = 'd:/test/mini'
big_filepath = 'd:/test/big'

def write_file(filepath, filesize):
    f = open(filepath, 'w')
    for i in range(0, filesize):
        f.write('a')
    f.flush()
    f.close()

def create_minfiles():
    for i in range(0, filenums):
        fullpath = os.path.join("%s/%s.txt" % (mini_filepath, i))
        write_file(fullpath, 1024)

def create_bigfiles():
    fullpath = os.path.join("%s/%s.txt" % (big_filepath, 'big'))
    write_file(fullpath, 1024 * 1024 * 100)

if __name__ == '__main__':
    time11 = time.time()
    create_minfiles()
    time12 = time.time()
    print('mini file generate time:', time12 - time11)

    time21 = time.time()
    create_bigfiles()
    time22 = time.time()
    print('big file generate time:', time22 - time21)
