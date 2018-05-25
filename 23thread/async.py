# -*- coding: utf-8 -*-
# Author: XuMing <xuming624@qq.com>
# Brief: 
import time
from multiprocessing import Pool


def function(index):
    print('Start process: ', index)
    time.sleep(3)
    print('End process', index)


if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in range(14):
        pool.apply_async(function, (i,))

    print("Started processes")
    pool.close()
    pool.join()
    print("Subprocess done.")