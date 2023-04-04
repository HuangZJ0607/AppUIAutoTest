import sys, os

from loguru import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Logger():
    def __init__(self):
        self.logger = logger
        self.logger.remove()
        self.logger.add(sys.stdout,
                        format="<green>{time:YYYYMMDD HH:mm:ss}</green> | "  # 颜色>时间®
                               "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 模块名.方法名
                               ":<cyan>{line}</cyan> | "  # 行号
                               "<level>{level}</level> | "  # 等级
                               "<level>{message}</level>",  # 日志内容
                        )
        # 输出到文件的格式,注释下面的add',则关闭日志写入
        self.logger.add(BASE_DIR + "/Log/run_log.Log", level='DEBUG',
                        format='{time:YYYYMMDD HH:mm:ss} | '  # 时间
                               '{module}.{function}:{line} | {level} | {message}',
                        rotation="10 MB")

    def get_logger(self):
        return self.logger


if __name__ == "__main__":
    logger = Logger().get_logger()
    logger.info("this is a info message")
    logger.debug("this is a debug message")
    logger.error("this is a error message")
