import os
import json

# Path to the directory containing the transcription files
directory_path = r'C:\Users\Brook\Downloads\pixel9'
output_file_path = os.path.join(directory_path, 'bundle.txt')

def process_transcription_files():
    with open(output_file_path, 'w') as bundle_file:
        # Iterate over all files in the directory
        for filename in os.listdir(directory_path):
            if filename.endswith('_transcription.json'):
                file_path = os.path.join(directory_path, filename)
                
                # Open and read the JSON file
                with open(file_path, 'r') as json_file:
                    data = json.load(json_file)
                    #now convert the string to a json object
                    response = json.loads(data)
                    # Assuming the transcription text is stored under a specific key
                    paragraphs = response['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']

                    if paragraphs is None:
                        continue
                    if len(paragraphs) == 0:
                        continue

                    #get the original url from the metadata file
                    metadata_file_path = os.path.join(directory_path, filename.replace('_transcription.json', '.json'))
                    url = ""
                    with open(metadata_file_path, 'r') as metadata_file:
                        metadata = json.load(metadata_file)
                        url = "https://www.tiktok.com/@" + metadata['author']['uniqueId'] + "/video/" + metadata['id']

                    # Process each paragraph
                    for paragraph in paragraphs:
                        for sentence in paragraph['sentences']:
                            cleaned_sentence = sentence['text'].replace('\n', ' ').strip()
                            if cleaned_sentence:  # Ensure the paragraph is not empty
                                # Write the filename and paragraph to the bundle file
                                bundle_file.write(f"{url}:{cleaned_sentence}\n")

# Run the processing function
process_transcription_files()