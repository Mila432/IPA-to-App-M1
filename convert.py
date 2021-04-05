# -*- coding: utf-8 -*-
import os
import sys
import time
import zipfile

def fixts(z, o):
	for f in zipfile.ZipFile(z, 'r').infolist():
		fullpath = os.path.join(o, f.filename)
		if not os.path.isfile(fullpath):	continue
		date_time = time.mktime(f.date_time + (0, 0, -1))
		os.utime(fullpath, (date_time, date_time))

def work(ipafile):
	appname=None
	with zipfile.ZipFile(ipafile, 'r') as fzip:
		for f in fzip.namelist():
			if '.app' not in f:	continue
			if appname is None:
				appname=f.split('/')[1]
			fzip.extract(f, 'tmp')
	fixts(ipafile,'tmp')
	pwd=os.getcwd()
	os.chdir('tmp')
	os.chmod(r'Payload/%s/%s'%(appname,appname.split('.')[0]), 0777)
	os.rename('Payload','Wrapper')
	os.symlink('Wrapper/%s'%(appname),'WrappedBundle')
	os.chdir(pwd)
	os.rename('tmp',appname)

if __name__ == "__main__":
	work(sys.argv[1])