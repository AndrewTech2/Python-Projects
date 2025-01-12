import streamlit, pytubefix

streamlit.title("YouTube Video Downloader")
url = streamlit.text_input(label='YouTube URL:', placeholder='YouTube URL')
if url:
    video = pytubefix.YouTube(url=url)
    download = streamlit.button('Download Video')
    if download:
        video.streams.get_highest_resolution().download(".", f'{video.title}.mp4')
        streamlit.success('File downloaded!')