import subprocess
import os

"""
Downloader for YouTube songs and playlists using yt-dlp.
Requires yt-dlp_x86.exe to be in the same directory as this script.
Automatic updates will be performed to ensure the latest version of yt-dlp is used.


Enter the URL of the YouTube playlist or song you want to download. 
The script will download the audio in MP3 format and save it to the specified directory.
Enter 'p' to download a playlist or 's' to download a single song.
"""


# Auto updates to remove errors
os.chdir("C:")      # Pref dir
subprocess.run('yt-dlp_x86.exe -U', shell=True)

dec = input("p to import playlist, s to import song")
if dec == "p":
    # Playlist -> playlist folder
    try:
        os.chdir('C:c')
        URL = input('Enter Playlist URL: ')
        Playlist_name = input('Enter playlist name: ')
        Playlist = os.mkdir(str(Playlist_name))
        subprocess.run(
            'yt-dlp_x86.exe --yes-playlist --extract-audio --audio-format mp3 --audio-quality 0 -o "C:' + str(
                Playlist) + '%(playlist_index)s - %(title)s.%(ext)s" "' + str(URL) + '"')

    except FileExistsError:
        print(f"Directory '{Playlist}' already exists.")

    except PermissionError:
        print(f"Permission denied: Unable to create '{Playlist}'.")

    except Exception as e:
        print(e)

elif dec == "s":
    # Single song to dir
    try:
        os.chdir('C:')
        URL = input('Enter YouTube URL: ')
        subprocess.run('yt-dlp_x86.exe --extract-audio --audio-format mp3 --audio-quality 0 -o "%(title)s.%(ext)s" "' + str(URL) + '"', shell=True)
        print("Successfully downloaded")

    except Exception as e:
        print(e)

else:
    print("Invalid input; 'p' for playlist or 's' for single song")
    quit()
