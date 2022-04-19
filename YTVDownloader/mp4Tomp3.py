#-*- coding:utf-8 -*-
#!/usr/bin/python
# Ref : https://codingdiksha.com/convert-mp4-video-to-mp3-audio-python-moviepy-script/
from moviepy.editor import *

def checkDirectory(source, target="mp3"):
    path = '{currentDirectory}/{source}/{target}'.format(currentDirectory=os.getcwd(), source=source, target=target)
    print(path)
    isExist = os.path.exists(path)
    if (not isExist):
        os.makedirs(path)
    return path

def listSource(source):
    rtnList = []
    sourceOfTarget = source
    ln = len(source.split('/'))
    if (ln == 1):
        sourceOfTarget = '{current}/{source}'.format(current=os.getcwd(), source=source)
    for root, dirs, files in os.walk(sourceOfTarget):
        for file in files:
            if file.endswith(".mp4"):
                rtnList.append(os.path.join(root, file))
    return rtnList

def convertMp4ToMp3(source, target="mp3"):
    target = checkDirectory(source, target)
    mp4Files = listSource(source)
    for file in mp4Files:
        mp4_file = file
        file_head, file_tail = os.path.split(mp4_file)
        mp3_file = '{target}/{filename}{ext}'.format(target=target, filename=os.path.splitext(file_tail)[0], ext='.mp3')

        videoclip = VideoFileClip(mp4_file)
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3_file)

        audioclip.close()
        videoclip.close()
        print("Done : ", mp3_file)

if __name__ == "__main__":
    source = input("Enter directory of source : ")
    target = input("Enter sub directory of target(only name) : ")
    convertMp4ToMp3(source=source, target=target)