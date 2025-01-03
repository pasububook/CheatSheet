"""
==========================================================================
# 機能
  指定されたディレクトリを探索し、結果を変数(: files) に格納します

# 変数
| 変数名 | 内容 | 例 |
| --- | --- | --- |
| directory | ファイルを探索するディレクトリ | data/directory |
==========================================================================
"""

import os

# ファイルを探索するディレクトリ
directory = ""

# ディレクトリ内のファイルを取得
files = []
if directory:
    for root, dirs, file_names in os.walk(directory):
        for file_name in file_names:
            file_path = os.path.join(root, file_name).replace('\\', '/')
            files.append(file_path)
else:
    print("ディレクトリが指定されていません。")
