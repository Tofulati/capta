from pytube import YouTube

def grabYT(link):
    yt = YouTube(f'"{link}"')

    try:
        title = yt.title
        author = yt.author
        print(f'Found video: {title} - {author}')
        yt = yt.streams.filter(
            only_video=True,
            file_extension='mp4'
            ).first()

    except ValueError:
        raise ValueError("\nYouTube link invalid.")
    
    yt.download(output_path='temp', filename='temp.mp4')
    print("\nmp4 retrieved.")

# def grabLINK(link):
    