import datetime
import os
import logging
import shutil
from dateutil.relativedelta import relativedelta
from zipfile import ZipFile

logPath = os.getcwd()+'/logs/'
LOG_FILENAME = logPath+'logger.log'

dirPath = os.getcwd()+'/prateek/'
backupDuration = 1 ### In months
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)
toDay=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
logging.debug(toDay+"Starting Daily Cron For Deleting Older Backups")
datediffe=datetime.datetime.now()-relativedelta(months=backupDuration)
dirtodel=datediffe.strftime('%Y-%m-%d')+'.txt'
delPath = os.path.join(dirPath,dirtodel)
isfile = os.path.isfile(delPath)
if(isfile):
	logging.debug(toDay+" Starting deletion of folder "+delPath)
	os.unlink(delPath)
	msgOS = ' Completed folder deletion '
else:	
	msgOS = ' File Not Present '
logging.debug(toDay+msgOS+delPath)	