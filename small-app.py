import os
from builtins import len

import sys
#
# if sys.argv[1]:
#     path = sys.argv[1]
#     print("path: " + path)
# else:

path = 'E:\\BaiduNetdiskDownload\\海底小纵队英文版93集\\S3季18集（带字幕）'

for root, dirs, files in os.walk(path):
    files.sort()
    i = 0
    k = 1
    while i < len(files):
        if files[i].__contains__('Octonauts_'):
            new_filename = files[i][len('Octonauts_'):-4]
        else:
            new_filename = files[i][:-4]

        # print(new_filename)

        cmd = 'D:/Tools/mkvtoolnix\mkvmerge.exe --ui-language zh_CN --output ' \
              '^"%(root)s\%(new)s.mkv^" --language 0:und ^"^(^" ^"%(root)s\%(file2)s^" ' \
              '^"^)^" --language 0:und --language 1:und ^"^(^" ^"%(root)s\%(file1)s^" ^"^)^" --track-order 0:0,' \
              '1:0,1:1' % {"root": root, "new": new_filename, "file1": files[i], "file2": files[i+1], "id": i}

        # print(cmd)
        os.system(cmd)
        i = i + 2
