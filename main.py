from pytube import YouTube
import os
from pydub import AudioSegment

def convert_to_mp3(input_file, output_file, sample_rate=44100):
    # Load the audio file
    audio = AudioSegment.from_file(input_file)
    
    # Set the sample rate
    audio = audio.set_frame_rate(sample_rate)
    
    # Export the audio file as MP3
    audio.export(output_file, format="mp3")

if __name__ == '__main__':
    while True:
        # URL input from user 
        video = YouTube(str(input("Enter the URL of the video you want to download: \n>> "))) 
        
        # Extract only audio
        print ("Extracting audio...")
        audio_stream = video.streams.filter(only_audio=True).first() 
        
        # Define destination directory
        destination = os.path.join("C:", os.sep, "Users", os.getlogin(), "Music")
        
        # Download the audio file
        print ("Downloading file...")
        out_file = audio_stream.download(output_path=destination) 
        
        # Define new file name
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        
        # Convert to MP3 with a consistent sample rate
        convert_to_mp3(out_file, new_file)
        
        # Remove the original downloaded file
        os.remove(out_file)
        
        # Result of success 
        print(video.title + " has been successfully downloaded and converted to MP3 with a sample rate of 44100 Hz.")
