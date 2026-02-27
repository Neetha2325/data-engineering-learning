import logging
import file2 as f2

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
fh=logging.FileHandler('File1.log')
fh.setFormatter(f)

logger.addHandler(fh)

logger.debug("Start of logger file")
logger.debug("Name:%s",f2.name)
logger.debug("GPA:%s",f2.gpa)
logger.debug("End of logger file ")
