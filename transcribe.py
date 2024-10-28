import os
import asyncio
from deepgram import (
    DeepgramClient,
    DeepgramClientOptions,
    PrerecordedOptions,
    FileSource,
)
from deepgram.utils import verboselogs
from transformers import pipeline
import httpx
import json
# Your Deepgram API key
DEEPGRAM_API_KEY = os.getenv('DEEPGRAM_API_KEY')

# Check if the token was retrieved successfully
if DEEPGRAM_API_KEY:
    print("DEEPGRAM_API_KEY retrieved successfully.")
else:
    print("DEEPGRAM_API_KEY not found. Please set the environment variable.")

# Path to the directory containing the videos
video_directory = r'C:\Users\Brook\Downloads\pixel9'

# Initialize the summarization pipeline

async def transcribe_video(file_path):
    output_path = file_path.replace(".mp4", "_transcription.json")
    if os.path.exists(output_path):
        return
    # Open the video file
    with open(file_path, 'rb') as audio:
        # Send the audio to Deepgram for transcription
        config: DeepgramClientOptions = DeepgramClientOptions(
            verbose=verboselogs.SPAM,
        )
        deepgram: DeepgramClient = DeepgramClient(DEEPGRAM_API_KEY, config)
        # OR use defaults
        # deepgram: DeepgramClient = DeepgramClient()

        # STEP 2 Call the transcribe_file method on the rest class
        with open(file_path, "rb") as file:
            buffer_data = file.read()

        payload: FileSource = {
            "buffer": buffer_data,
        }

        options: PrerecordedOptions = PrerecordedOptions(
            model="nova-2",
            smart_format=True,
            paragraphs=True,
            utterances=True,
            punctuate=True,
            diarize=True,
        )

        response = deepgram.listen.rest.v("1").transcribe_file(
            payload, options, timeout=httpx.Timeout(300.0, connect=10.0)
        )
        data = response.to_json(indent=4)
        with open(output_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)

async def transcribe_all_videos():
    # Iterate over all files in the directory
    for filename in os.listdir(video_directory):
        if filename.endswith('.mp4'):  # Assuming the videos are in .mp4 format
            video_path = os.path.join(video_directory, filename)
            await transcribe_video(video_path)

# Run the transcription and summarization process
asyncio.run(transcribe_all_videos())