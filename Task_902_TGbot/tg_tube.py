from pytube import YouTube
import os.path

def video_download(url, res):
    yt = YouTube(url)
    # video_res = ['720p', '480p', '360p', '240p', '144p']
    video_list = yt.streams.get_by_resolution(res)
    file_path = f'/{yt.title}.mp4'
    video_list.download()

    # Ждем скачивания файла
    while False:
        os.path.exists(file_path)
    print('Файл успешно скачан')

    return f'{yt.title}.mp4'

    # audio_list = yt.streams.filter(only_audio=True)
    # print(audio_list)