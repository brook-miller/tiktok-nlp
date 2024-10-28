from TikTokApi import TikTokApi
from yt_dlp import YoutubeDL
import asyncio
import os
from pathlib import Path
import json

ms_token = os.getenv('ms_token')

# Check if the token was retrieved successfully
if ms_token:
    print("ms_token retrieved successfully.")
else:
    print("ms_token not found. Please set the environment variable.")
    
base_path = r"C:\Users\Brook\Downloads"

async def user_example(username):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
        user = api.user(username)
        user_data = await user.info()
        print(user_data)
        Path(username).mkdir(exist_ok=True)
        ydl_opts = {
            'outtmpl': username + '\\%(uploader)s_%(id)s_%(timestamp)s.%(ext)s',
        }
        async for video in user.videos(count=30):
            print(video)
            print(video.as_dict)

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download(["https://www.tiktok.com/@" + video.author.username + "/video/" + video.id])
            #sleep for 30 secs
            
            #data = api.video.bytes # bytes of the video
            #with open(username + "\{}.mp4".format(count), 'wb') as output:
            #    output.write(await video.bytes())

async def tagexample(query):
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3, headless=False)
        Path(os.path.join(base_path, query)).mkdir(exist_ok=True)
        ydl_opts = {
            'outtmpl': base_path + "\\" + query + '\\%(uploader)s_%(id)s.%(ext)s',
        }
        tag = api.hashtag(name=query)
        async for video in tag.videos(count=200):
            json_filename = f"{video.author.username}_{video.id}.json"
            
            # Save video metadata to a JSON file
            with open(os.path.join(base_path, query, json_filename), 'w') as json_file:
                json.dump(video.as_dict, json_file, indent=4)

            with YoutubeDL(ydl_opts) as ydl:
                ydl.download(["https://www.tiktok.com/@" + video.author.username + "/video/" + video.id])


asyncio.run(tagexample("pixel9"))

# asyncio.run(user_example("breakyourbudget"))
