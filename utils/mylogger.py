#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
#=============================================================================
# FileName:     mylogger.py
# Desc:         日志记录函数，可以滚动打包日志
# Author:       leyle
# Email:        leyle@leyle.com
# HomePage:     http://www.leyle.com/
# Git_page:     https://github.com/leyle
# Version:      0.0.1
# LastChange:   2014-12-08 10:13:38
# History:      
#=============================================================================
'''

import logging
import logging.handlers
import sys
import os
import time

LOGGING_MSG_FORMAT = "%(name)s %(levelname)s %(asctime)s: %(message)s"
LOGGING_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
MAXBYTE = 1024*1024*50  #50M
BACKUPCOUNT = 20  #循环备份的最大数

def get_logger(logname):
    root_logger = logging.getLogger(logname)
    if len(root_logger.handlers) == 0:
        path = os.path.join(sys.path[0], 'logs/')
        if not os.path.isdir(path):
            os.mkdir(path)
        filename = path + logname + ".log"
        handler = logging.handlers.RotatingFileHandler(
                    filename,
                    mode = "a",
                    maxBytes = MAXBYTE,
                    backupCount = BACKUPCOUNT,
                    encoding = "utf-8"
                    )
        fmter = logging.Formatter(LOGGING_MSG_FORMAT, LOGGING_DATE_FORMAT)
        handler.setFormatter(fmter)
        root_logger.addHandler(handler)
        root_logger.setLevel(logging.DEBUG)

    line_name = "%s" % logname
    return logging.getLogger(line_name)

def test():
    mylog = get_logger("log_name")
    for i in range(0, 1000):
        mylog.info("%d" % i)

if __name__ == "__main__":
    test()
