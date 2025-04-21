import os
import subprocess
from yt_dlp import YoutubeDL


def update_ytdlp():
    subprocess.call(['python3', '-m', 'pip', 'install', '--upgrade', 'yt-dlp'])


def download_playlist(playlist_url, download_path):
    # Update yt-dlp
    update_ytdlp()

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': False,  # Ensure it downloads full playlist
    }

    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(playlist_url, download=False)
        playlist_title = info_dict.get('title', 'Untitled Playlist')
        print(f"Downloading playlist: {playlist_title}")
        ydl.download([playlist_url])

    print("Download and conversion to MP3 completed!")


# Example usage
if __name__ == "__main__":
    playlist_url = input("Playlist link: ").strip()
    download_path = input("Download path: ").strip()
    download_playlist(playlist_url, download_path)
