import sys

python_2x ="Bu yazı sadece python 2 versiyonunda çalışır"
python_3x = "Bu yazı sadece python 3 sürümlerinde çalışır"
print(sys.version)
if sys.version_info.major < 3:
    print(python_2x)

else:
    print(python_3x)
    
    if "3.7.4" in sys.version:
        print("Version kontrolü ile 3.7 olduğunu öğrendik")
    else:
        print("çalışmadı")

"""sys modülü içinde sürüm denetlemeye
yarayan iki farklı degisken var. Bunlardan biri version, öbürü ise version_info.
Python3’te bu degiskenlerin su çıktıları verdiginiz biliyoruz:
version:
`3.5.1 (default, 20.04.2016, 12:24:55)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-3)] on linux'
version_info:
sys.version_info(major=|major3|, minor=|minor3|, micro=|micro3|, releaselevel='final', serial="""

