
# TikTok Video Transcription and Analysis

This project provides tools to transcribe TikTok videos, process the transcriptions, and analyze the content for specific keywords.

## Directory Structure


### `transcribe.py`

This script handles the transcription of TikTok videos using the Deepgram API.

- **Functions:**
  - `transcribe_video(file_path)`: Transcribes a single video file and saves the transcription as a JSON file.
  - `transcribe_all_videos()`: Iterates over all `.mp4` files in the specified directory and transcribes them.

- **Usage:**
  ```sh
  python transcribe.py

## Files

### bundle.py
This script processes the transcription JSON files and bundles the transcriptions into a single text file.

Functions:

process_transcription_files(): Reads all transcription JSON files, extracts the text, and writes it to bundle.txt.
Usage:

###tiktok.ipynb
This Jupyter Notebook analyzes the transcriptions for specific keywords and visualizes the results using a bar chart.

Steps:

Load the dataset of TikTok sentences.
Count occurrences of specific keywords.
Plot the results using matplotlib.
Usage: Open tiktok.ipynb in Jupyter Notebook and run the cells.

tiktokdl.py
This script is intended for downloading TikTok videos. (Details not provided in the excerpts.)