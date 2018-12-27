import os

import os

for root, dirs, files in os.walk("E:\BaiduNetdiskDownload\海底小纵队英文版93集\S2季23集（带字幕）"):
    for file in files:
        print(file)
        if file.__contains__("S02E"):
            new_file
        for i in range(1, 10):
            cmd = 'D:/Tools/mkvtoolnix\mkvmerge.exe --ui-language zh_CN --output ' \
                  '^"E:\BaiduNetdiskDownload\海底小纵队英文版93集\S2季23集（带字幕）\S02E0%(id)d.mkv^" --language 0:und ^"^(^" ' \
                  '^"E:\BaiduNetdiskDownload\海底小纵队英文版93集\S2季23集（带字幕）\Octonauts_S02E0%(id)d_*.srt^" ' \
                  '^"^)^" --language 0:und --language 1:und ^"^(^" ^"E:\BaiduNetdiskDownload\海底小纵队英文版93集\S2季23集' \
                  '（带字幕）\Octonauts_S02E0%(id)d_*.avi^" ^"^)^" --track-order 0:0,1:0,1:1' % {"id": i}
            os.system(cmd)

        for j in range(10, 23):
            cmd = 'D:/Tools/mkvtoolnix\mkvmerge.exe --ui-language zh_CN --output ' \
                  '^"E:\BaiduNetdiskDownload\海底小纵队英文版93集\S2季23集（带字幕）\S02E0%(id)d.mkv^" --language 0:und ^"^(^" ' \
                  '^"E:\BaiduNetdiskDownload\海底小纵队英文版93集\S2季23集（带字幕）\Octonauts_S02E0%(id)d_The_Colossal_Squid.srt^" ' \
                  '^"^)^" --language 0:und --language 1:und ^"^(^" ^"E:\BaiduNetdiskDownload\海底小纵队英文版93集\S2季23集' \
                  '（带字幕）\Octonauts_S02E0%(id)d_The_Colossal_Squid.avi^" ^"^)^" --track-order 0:0,1:0,1:1' % {"id": j}
            os.system(cmd)
