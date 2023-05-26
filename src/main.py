# using youtube-dl 2023.05.26.810 version

import os
import youtube_dl
import subprocess

def update_youtubedl():
    subprocess.call(['youtube-dl', '-U'])

def download_playlist(playlist_url, download_path):
    # Update youtube-dl
    update_youtubedl()

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        playlist_title = info_dict.get('title', 'Untitled Playlist')
        print(f"Downloading playlist: {playlist_title}")
        ydl.download([playlist_url])

    # Convert downloaded files to MP3 format
    print("Converting videos to MP3 format...")
    subprocess.call(['ffmpeg', '-i', f'{download_path}/*.%(ext)s', '-codec:a', 'libmp3lame', '-q:a', '2', f'{download_path}/*.mp3'])

    print("Conversion completed!")

# Example usage
playlist_url = input("Playlist link")
download_path = input("Download path")
download_playlist(playlist_url, download_path)