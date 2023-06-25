import os
import pandas as pd
import glob
import time
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from googletrans import Translator
import re
import torch

# Get the current file location
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths
input_directory = os.path.join(current_dir, 'jjTasks')
output_directory = input_directory

# Check if there are any raw_output_*.csv files
raw_files = glob.glob(os.path.join(input_directory, 'raw_output_*.csv'))
if len(raw_files) == 0:
    print("No raw_output_*.csv files found.")
    exit()

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

# Function to translate using the Google Translate API
def translate_with_api(comment):
    # Implement your code to use the Google Translate API here
    # Return the translated comment
    
    # Placeholder implementation
    return comment + ' (Translated with API)'

# Function to translate using the googletrans library (web scraping)
def translate_with_googletrans(comment):
    translator = Translator()
    try:
        translation = translator.translate(comment, src='zh-cn', dest='en')
        return translation.text
    except:
        return "Translation Error"

# Choose the translation method
use_googletrans = True  # Set to False if you want to use the API

# Get the list of files in the "jjTasks" folder
file_list = glob.glob(os.path.join(input_directory, 'raw_output_*.csv'))

# Extract the numeric part of the file names for sorting
numeric_part = lambda file_name: int(re.search(r'\d+', file_name).group())

# Sort the file list based on the numeric part of the file names
file_list.sort(key=numeric_part)

# List to store the processed Bert_analysis_#.csv files
processed_files = []

# Iterate over the files inside "jjTasks" and execute them with a delay
total_files = len(file_list)
for i, file_path in enumerate(file_list):
    file_name = os.path.basename(file_path)
    print(f"Processing file: {file_name}")
    
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    # Select only the 'comment' column for translation
    comments = df['comment'].tolist()
    
    # Remove extra spaces and symbols from comments
    cleaned_comments = [re.sub(r'[^\w\s]', '', str(comment).strip()) for comment in comments]
    
    # Translate comments
    translated_comments = []
    for comment in cleaned_comments:
        if use_googletrans:
            translated_comment = translate_with_googletrans(comment)
        else:
            translated_comment = translate_with_api(comment)
        translated_comments.append(translated_comment)
    
    # Perform sentiment analysis for each translated comment
    sentiment_scores = []
    for comment in translated_comments:
        if comment == "Translation Error":
            sentiment_scores.append(0)  # Assign a neutral sentiment score for failed translations
            continue
    
        token = tokenizer.encode(comment, return_tensors='pt', padding=True, truncation=True)
        result = model(token)
        rating = int(torch.argmax(result.logits)) + 1
        sentiment_scores.append(rating)
    
    # Add the sentiment scores and translated comments to the DataFrame
    df['Sentiment_Score (Translated)'] = sentiment_scores
    df['Translated_Comment'] = translated_comments
    
    # Modify column names
    df.rename(columns={'Sentiment_Score (Translated)': 'score', 'Sentiment_Score (Original)': 'Sentiment_Score_Orig'}, inplace=True)
    
    # Save the DataFrame to a new CSV file in the "jjTasks" folder
    output_file = os.path.join(input_directory, f"Bert_analysis_{i}.csv")
    df.to_csv(output_file, index=False)
    
    # Add the processed file to the list
    processed_files.append(output_file)
    
    print(f"Processing completed for file: {file_name}")
    
    # Calculate progress percentage
    progress = (i + 1) / total_files * 100
    print(f"Progress: {progress:.2f}%")
    
    if i != len(file_list) - 1:
        print("Waiting for 3 seconds before processing the next file...")
        time.sleep(3)

print("All files processed.")

# Delete the raw_output_#.csv files
for file in raw_files:
    os.remove(file)

# Combine the Bert_analysis_#.csv files into a single file
combined_df = pd.concat([pd.read_csv(file) for file in processed_files])

# Modify column names
combined_df.rename(columns={'Sentiment_Score (Translated)': 'score'}, inplace=True)

# Check if the 'Translated_Comment' column exists before dropping it
if 'Translated_Comment' in combined_df.columns:
    combined_df.drop(columns='Translated_Comment', inplace=True)

combined_output_file = os.path.join(input_directory, 'Final_BERT.csv')
combined_df.to_csv(combined_output_file, index=False)

# Delete the old Bert_analysis_#.csv files
bert_files = glob.glob(os.path.join(input_directory, 'Bert_analysis_*.csv'))
for file in bert_files:
    os.remove(file)

print("All files processed and cleaned up.")
