import glob
import os
from builtins import len

import sys
#
# if sys.argv[1]:
#     path = sys.argv[1]
#     print("path: " + path)
# else:

path = 'E:/BaiduNetdiskDownload/海底小纵队英文版93集/S3季18集（带字幕）'

os.chdir(path)

for f in glob.glob('*.mp4'):
    (short_name, extension) = os.path.splitext(f)
    # print(short_name, extension)
    if short_name.__contains__('Octonauts_'):
        new_filename = short_name[len('Octonauts_'):]

    cmd = 'D:/Tools/mkvtoolnix\mkvmerge.exe --ui-language zh_CN --output ' \
          '^"%(root)s/%(new)s.mkv^" --language 0:und ^"^(^" ^"%(root)s/%(file2)s.srt^" ' \
          '^"^)^" --language 0:und --language 1:und ^"^(^" ^"%(root)s/%(file1)s.mp4^" ^"^)^" --track-order 0:0,' \
          '1:0,1:1' % {"root": path, "new": new_filename, "file1": short_name, "file2": short_name}



    # print(cmd)
    os.system(cmd)

