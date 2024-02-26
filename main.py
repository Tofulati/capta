from utils import to_MP3
from utils import to_MP4
from utils import to_VID

def main():
    
    url = input("Enter video URL: ")

    try:    
        to_MP4.grabYT(url)
        to_MP3.grabYT(url)

    except ValueError: 
        raise ValueError("Invalid URL.")
    

if __name__ == "__main__":
    main()
