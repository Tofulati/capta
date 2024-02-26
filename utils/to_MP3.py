from pytube import YouTube

def grabYT(link):
    yt = YouTube(f'"{link}"')

    try:
        yt = yt.streams.filter(
            only_audio=True
            ).first()

    except KeyError:
        raise KeyError("YouTube link invalid.")
    
    yt.download(output_path='temp', filename='temp.mp3')
    
    print("mp3 retrieved.")