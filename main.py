from src.logger import Logger

_logger_obj = Logger('main')
logger= _logger_obj.get_logger()

logger.info('New updates ')
logger.error('error updating')
logger.warning('warning msg')
