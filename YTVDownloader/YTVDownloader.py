# -*- coding:utf-8 -*-
# !/usr/bin/python
# Ref : https://www.analyticsvidhya.com/blog/2022/02/youtube-video-downloader-using-python/
# SSL: CERTIFICATE_VERIFY_FAILED :: https://exerror.com/urllib-error-urlerror-urlopen-error-ssl-certificate_verify_failed-certificate-verify-failed-unable-to-get-local-issuer-certificate/

from pytube import YouTube
from pytube import Playlist
from pytube import Channel
import os
import mp4Tomp3 as convertor

def checkDirectory(target):
    if (target == ""): return
    currentDirectory = os.getcwd()
    path = currentDirectory + '/' + target
    isExist = os.path.exists(path)
    if (not isExist):
        os.makedirs(path)

def convertMp4ToMp3(target):
    convertor.convertMp4ToMp3(source=target, target="mp3")

def playlist(url, target, conv=False):
    playlist = Playlist(url)
    checkDirectory(target)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for video in playlist.videos:
        video.streams.filter(progressive=True,
                             file_extension='mp4').order_by(
            'resolution').desc().first().download()
    if (conv): convertMp4ToMp3(target=target)
    print("Done!!")

def video(url, target, conv=False):
    video_caller = YouTube(url)
    checkDirectory(target)
    print(video_caller.title)
    video_caller.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download()
    if (conv): convertMp4ToMp3(target=target)
    print("Done!!")

def channel(url, target):
    channel_videos = Channel(url)
    checkDirectory(target)
    print(f'Downloading videos by: {channel_videos.channel_name}')
    for video in channel_videos.videos:
        video.streams.filter(progressive=True,
                             file_extension='mp4').order_by(
            'resolution').desc().first().download()
    print("Done!!")

def video_voice_only(url, target):
    video_caller = YouTube(url)
    checkDirectory(target)
    print(video_caller.title)
    audio = video_caller.streams.filter(only_audio=True).first()
    out_path = audio.download(output_path=video_caller.title)
    new_name = os.path.splitext(out_path)
    os.rename(out_path, new_name[0] + ".mp3")
    print("Done!!")

def picture_only(url, target):
    video_caller = YouTube(url)
    checkDirectory(target)
    print(video_caller.title)
    video = video_caller.streams.filter(only_video=True).first()
    out_path = video.download(output_path=video_caller.title)
    new_name = os.path.splitext(out_path)
    os.rename(out_path, new_name[0] + ".mp4")
    print("Done!!")

if __name__ == "__main__":
    required = input("Enter 1.playlist to download playlist; \n"
                     "2.video to download a video \n"
                     "3.channel to download all videos from a channel \n"
                     "4.voice for only voice file \n"
                     "5.picture for picture only \n")
    if (required == "1" or required == "playlist"):
        url = input("Enter the url for whole playlist : ")
        target = input("Enter sub directory of target(only name) : ")
        conv = input("Are you want to convert mp4 to mp3(y/[N]) : ")
        if (conv.upper() == 'Y') : conv = True
        playlist(url=url, target=target, conv=conv)
    elif (required == "2" or required == "video"):
        url = input("Enter the url of the video : ")
        target = input("Enter sub directory of target(only name) : ")
        conv = input("Are you want to convert mp4 to mp3(y/[N]) : ")
        if (conv.upper() == 'Y') : conv = True
        video(url=url, target=target, conv=conv)
    elif (required == "3" or required == "channel"):
        url = input("Enter the url of the channel : ")
        target = input("Enter sub directory of target(only name) : ")
        channel(url=url, target=target)
    elif (required == "4" or required == "voice"):
        url = input("Enter the url of the video : ")
        target = input("Enter sub directory of target(only name) : ")
        video_voice_only(url=url, target=target)
    elif (required == "5" or required == "picture"):
        url = input("Enter the url of the video : ")
        target = input("Enter sub directory of target(only name) : ")
        picture_only(url=url, target=target)
    else:
        print("Invalid")