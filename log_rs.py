import logging
#设置日志的输出样式
import sys, logging

logging.basicConfig(level=logging.INFO,  # 日志等级　　　　　　　　　　　　　　　　　#　filename: 指定日志文件名
                    format='levelname:%(levelname)s filename: %(filename)s '
                           'outputNumber: [%(lineno)d]  thread: %(threadName)s output msg:  %(message)s'  # 日志内容
                           ' - %(asctime)s', datefmt='[%d/%b/%Y %H:%M:%S]',  # 日志时间
                    filename='./loggmsg.log')  # 存放路径

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("this is a info log")
    logger.info("this is a info log 1")