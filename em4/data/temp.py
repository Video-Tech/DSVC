import os

files = os.listdir('eval1')

for f in files:
    if f.startswith("video"):
        os.system('ffmpeg -i eval1/'+f+' -vf scale=352x288 eval/'+f)
