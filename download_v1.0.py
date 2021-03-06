import pandas as pd
import numpy as np
from pytube import YouTube

def YouTube_download(need_artist, artist_work_list, id_file):
    for i in need_artist:
        for j in range(artist_work_list[i,0], artist_work_list[i,1]):
            try:
                yt = YouTube('https://youtube.com/watch?v=' + id_file.iloc[j,0])
                audio_stream = yt.streams.filter(file_extension='mp4', only_audio=True).first()
                vedio_stream = yt.streams.filter(res='360p',fps=30, file_extension='mp4').first()
                # show the audio/vedio type detail
                print(audio_stream)
                print(vedio_stream)
                if (audio_stream is not None) and (vedio_stream is not None):
                    print("downloading audio ......")
                    audio_stream.download('audio') # , filename="test_audio_" + str(i) + "_" + str(j)
                    print("downloading vedio ......")
                    vedio_stream.download('vedio') # , filename="test_vedio" + str(i) + "_" + str(j) 
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