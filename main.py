import dearpygui.dearpygui as dpg
from pytube import YouTube, Playlist

dpg.create_context()
dpg.create_viewport(title='YouTube Downloader', width=600, height=400)

def video():
    video_link = dpg.get_value(link)
    path = dpg.get_value(download_path)

    yt = YouTube(video_link)
    yt.streams.get_highest_resolution().download(path)
    print("Downloaded:", yt.title)

def playlist():
    playlist_link = dpg.get_value(link)
    path = dpg.get_value(download_path)

    p = Playlist(playlist_link)

    for video in p.videos:
        video.streams.get_highest_resolution().download(path)
        print("Downloaded:", video.title)

with dpg.window(label='YouTube Download', tag="Window"):
    dpg.add_text("Enter YouTube video/playlist link to be downloaded")
    link = dpg.add_input_text(hint="https://www.youtube.com/")
    dpg.add_text("Enter directory to save video/playlist to")
    download_path = dpg.add_input_text(default_value="D:\Downloads")
    dpg.add_text("")
    with dpg.group(horizontal=True):
        dpg.add_button(label="Download Video", callback=video)
        dpg.add_button(label="Download Playlist", callback=playlist)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Window", True)
dpg.start_dearpygui()
dpg.destroy_context()
