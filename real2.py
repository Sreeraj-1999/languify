#Extracting audio from the video

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
import moviepy.editor as mp

# Input video file
input_video_file = r"C:\Users\SREERAJ\OneDrive\Desktop\Languify\LinguaCraft\hindi_video.mp4"

# Output audio file
output_audio_file = "extracted_audio.mp3"

# Use FFmpeg to extract audio from the video
ffmpeg_extract_audio(input_video_file, output_audio_file)

# You can use moviepy's audio tools if you need further audio processing
audio_clip = mp.AudioFileClip(output_audio_file)

# To save the audio in a different format (e.g., WAV)
output_audio_file_wav = "extracted_audio.wav"
audio_clip.write_audiofile(output_audio_file_wav)

print("Audio extracted and saved as", output_audio_file_wav)


#Audio to text conversion

import speech_recognition as sr

# Define the audio file you want to convert to text
audio_file = "extracted_audio.wav"  # Replace with your audio file
source_language = "hi-IN"  # Replace with the appropriate source language code

# Initialize the recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio = sr.AudioFile(audio_file)

# Convert audio to text using Google Web Speech API
try:
    with audio as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data, language=source_language)
        print("Recognized text in the source language:")
        print(text)

        # Save the recognized text to a text file
        with open("recognized_text.txt", "w", encoding="utf-8") as text_file:
            text_file.write(text)

        print("Recognized text saved to recognized_text.txt")

except sr.UnknownValueError:
    print("Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")


#Translation

from googletrans import Translator
from gtts import gTTS


# Read the saved text file
with open("recognized_text.txt", "r", encoding="utf-8") as text_file:
    hindi_text = text_file.read()

# Translate Hindi text to Malayalam using the Google Translate API
translator = Translator()
translation = translator.translate(hindi_text, src="hi", dest="en")
english_text = translation.text
translation = translator.translate(english_text, src="en", dest="ml")
malayalam_text = translation.text
# Convert the text to speech using gTTS
tts = gTTS(text=malayalam_text, lang='ml')

# Save the generated speech to an audio file
tts.save("translated_audio.mp3")

# Play the translated audio
#os.system("start translated_audio.mp3")  # Adjust this line based on your OS (Windows in this example)

#mixing the translated audio with video
from moviepy.editor import VideoFileClip, AudioFileClip, clips_array

# Load the original video
video = VideoFileClip(r"C:\Users\SREERAJ\OneDrive\Desktop\Languify\LinguaCraft\hindi_video.mp4")  # Replace with your original video file

# Load the translated audio
audio = AudioFileClip(r"C:\Users\SREERAJ\Downloads\audio (2).wav")  # Replace with your translated audio file

# Set the audio of the video to the translated audio
video = video.set_audio(audio)

# Write the final video with the translated audio
video.write_videofile("output_video_with_audio.mp4", codec="libx264", audio_codec="aac")

print("Video with translated audio created as output_video_with_audio.mp4")

#Play the video
from moviepy.editor import VideoFileClip

# Load the video with audio
video_file = "output_video_with_audio.mp4"  # Replace with the path to your video file

# Create a VideoFileClip
video_clip = VideoFileClip(video_file)

# Play the video in a loop
video_clip.preview()

# Close the video preview when finished
video_clip.close()
