from pytube import YouTube


# Get user youtube video
video_url = input("Enter video url: ")
yt = YouTube(video_url)


# Choosing which stream to download
stream_select = input("Would you like audio only or both? \n")

if stream_select in ['audio', 'audio only', 'only audio']:
    stream = yt.streams.get_audio_only()
    print("Downloading %s audio only", yt.title)

else:
    stream = yt.streams.get_highest_resolution()
    print("Downloading %s", yt.title)


# Downloading here
stream.download(output_path="downloaded")


# Final output
print("Done downloading!")
