import pandas as pd
import numpy as np
from pytube import YouTube
import subprocess

def YouTube_download(need_artist, artist_work_list, id_file):
    for i in need_artist:
        for j in range(artist_work_list[i,0], artist_work_list[i,1]):
            try:
                url = 'https://youtube.com/watch?v=' + id_file.iloc[j,0]
                yt = YouTube(url)
                vedio_stream = yt.streams.get_by_itag('18')
                # show the audio/vedio type detail
                print(vedio_stream)
                if vedio_stream is not None:
                    print("downloading vedio and audio ......")
                    command = r'youtube-dl -o "vedio\%(title)s.%(ext)s" -f 18 -x -k --audio-format "mp3" ' + url
                    subprocess.Popen(command,shell=True)
            except:
                print('Ops! something wrong happens with this artists')

def load_Youtube_id(id_path, NUM_ARTIST):
    id_file = pd.read_csv(id_path, header=None, sep='@')
    artist_work_list = np.zeros((NUM_ARTIST,2), dtype=np.int)    # used to record the start and the end location of each artist's works

    artist_count = 0
    for index, row in id_file.iterrows():
        if row[0].startswith('# new artist'):  
            artist_work_list[artist_count, 0] = index + 1
            if artist_count - 1 >= 0:
                artist_work_list[artist_count - 1, 1] = index
            artist_count += 1

    artist_work_list[artist_count - 1, 1] = id_file.shape[0]

    return id_file, artist_work_list

def main():
    # you can change your down load list here. Each file contains 500 artists
    # id_path = r'YouTube-music-video-5M/youtube_ids/youtube_video_ids_13_247658.txt'
    # NUM_ARTIST = 500 # a constant that shows how many artists (singers) are in one id list

    # the following is a demo
    id_path = r'YouTube-music-video-5M/youtube_ids/test.txt'
    NUM_ARTIST = 2  # a constant that shows how many artists (singers) are in one id list
    id_file, artist_work_list = load_Youtube_id(id_path, NUM_ARTIST)
    
    # print(artist_work_list)
    # decide which artist's song you need
    need_artist = range(0,2)    # this means you want the songs of artist 0 and artist 1 

    YouTube_download(need_artist, artist_work_list, id_file)

if __name__ == '__main__':
    main()