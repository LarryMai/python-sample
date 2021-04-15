# see  [Argparse 教學](https://docs.python.org/zh-tw/3/howto/argparse.html)
# or [Day-12 程式運行：解析命令列參數](https://ithelp.ithome.com.tw/articles/10221694)
import os
import argparse
import datetime
import json

config_file_path=""
parser = argparse.ArgumentParser()

# 加入參數範本
    # -t [value:yyyy-mm-dd]
    # --today [value:yyyy-mm-dd]
parser.add_argument(
    # 短參數
    '-t',
    # 長參數
    '--today',
    # 參數說明
    help='set today in yyyy-mm-dd format',
    # 如果參數需要由字串解析成指定型態或物件，使用 type 參數
    type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d')
)

