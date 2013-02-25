
import socket 
import urllib2
import os
import shutil
import re
import urllib,ftplib
import time
from datetime import datetime, date


def wfile(file,cont):
	w = open(file,'a')
	w.write('\n'+cont)
	w.close
def wlog(cont):
	 wfile('log.txt',str(datetime.now())+'  :'+cont)

if __name__ == '__main__':

	print 'ashok'