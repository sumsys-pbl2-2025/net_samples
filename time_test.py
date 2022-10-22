# -*- coding: utf-8 -*-
# time_test.py for Python 3  - スリープ前後で時刻を記録し、経過時間（秒）を表示。
#
import time

start_time = time.time()

time.sleep(3.75)

end_time = time.time()
elapsed_time = end_time - start_time
print('Start: {0}, End: {1}, Elapsed: {2} seconds'.
        format(start_time, end_time, elapsed_time))

