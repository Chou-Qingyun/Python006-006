from datetime import *
import time
import logging
from pathlib import Path

log_path = "/var/log1/python-"
def record_log():
        time_item =  time.strftime('%Y_%m_%d', time.localtime())
        file_path  = log_path + time_item
        file_name =  file_path + "/logging_test_" + time.strftime('%H%M%S') + ".log"
        p_dir = Path(file_path)
        if p_dir.exists() == False:
            p_dir.mkdir(mode=0o777)
        logging.basicConfig(filename=file_name, format="%(asctime)s %(message)s  %(lineno)d", datefmt="%Y-%m-%d %H:%M:%S",level=logging.DEBUG)
        logging.debug('这是调用函数的时间')
        logging.info('这是调用函数的时间-info')
        logging.warning('这是调用函数的时间-warning')
record_log()