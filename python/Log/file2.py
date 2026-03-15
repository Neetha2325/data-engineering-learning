import logging 

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

f=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
fh=logging.FileHandler('file2_log.log')
fh.setFormatter(f)

logger.addHandler(fh)

logger.info('Start of file2')

name="XYZ"
gpa=9.2

logger.info("End of file2")
