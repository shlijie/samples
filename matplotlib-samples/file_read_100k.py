# coding:utf-8
import os
import time

filenums = 102400
mini_filepath = 'd:/test/mini'
onfile_filepath = 'd:/test/big/big.txt'

def read_file(filepath):
    f = open(filepath, 'r')
    content = f.read()
    f.close()

def read_minfiles(path):
    for i in range(0, filenums):
        fullpath = os.path.join("%s/%s.txt" % (path, i))
        read_file(fullpath)

if __name__ == '__main__':
    time11 = time.time()
    read_minfiles(mini_filepath)
    time12 = time.time()
    print('minifile read time:', time12 - time11)

    time21 = time.time()
    read_file(onfile_filepath)
    time22 = time.time()
    print('onefile read time:', time22 - time21)
