# -*- coding: utf-8 -*-
"""Speaker_Dialogue_Summarization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MQqeXVo9JSNVqaTrnV30d7TExhXbsfXI
"""

pip install summa

#Importing libraries
from summa import summarizer
from summa import keywords
import pandas as pd

from google.colab import drive
drive.mount("/content/drive")

#Read csv file
df = pd.read_csv("/content/drive/My Drive/MeetingSummary/simpsons_dataset.csv")
print(df)

type(df.spoken_words[0])

len(df)

#Checking for null rows
df.isnull().sum()

#Dropping blank rows
df.dropna(inplace=True)

len(df)

df.reset_index(inplace=True)
df.drop(['index'], axis=1)

df.isnull().sum()

#Selecting only first 3600 rows to test
test_df = df[:3600]
test_df.drop(["index"], axis = 1)

#Creating a list of all unique speakers
unique_speakers = test_df.raw_character_text.unique().tolist()
unique_speakers

len(unique_speakers)

#Creating a dictionary for abbreviations
abbreviation_mapping = {"ain't": "is not", "aren't": "are not","can't": "cannot", "'cause": "because", "could've": "could have", "couldn't": "could not",
                         
                           "didn't": "did not", "doesn't": "does not", "don't": "do not", "hadn't": "had not", "hasn't": "has not", "haven't": "have not",

                           "he'd": "he would","he'll": "he will", "he's": "he is", "how'd": "how did", "how'd'y": "how do you", "how'll": "how will", "how's": "how is",

                           "I'd": "I would", "I'd've": "I would have", "I'll": "I will", "I'll've": "I will have","I'm": "I am", "I've": "I have", "i'd": "i would",

                           "i'd've": "i would have", "i'll": "i will",  "i'll've": "i will have","i'm": "i am", "i've": "i have", "isn't": "is not", "it'd": "it would",

                           "it'd've": "it would have", "it'll": "it will", "it'll've": "it will have","it's": "it is", "let's": "let us", "ma'am": "madam",

                           "mayn't": "may not", "might've": "might have","mightn't": "might not","mightn't've": "might not have", "must've": "must have",

                           "mustn't": "must not", "mustn't've": "must not have", "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock",

                           "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not", "sha'n't": "shall not", "shan't've": "shall not have",

                           "she'd": "she would", "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", "she's": "she is",

                           "should've": "should have", "shouldn't": "should not", "shouldn't've": "should not have", "so've": "so have","so's": "so as",

                           "this's": "this is","that'd": "that would", "that'd've": "that would have", "that's": "that is", "there'd": "there would",

                           "there'd've": "there would have", "there's": "there is", "here's": "here is","they'd": "they would", "they'd've": "they would have",

                           "they'll": "they will", "they'll've": "they will have", "they're": "they are", "they've": "they have", "to've": "to have",

                           "wasn't": "was not", "we'd": "we would", "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", "we're": "we are",

                           "we've": "we have", "weren't": "were not", "what'll": "what will", "what'll've": "what will have", "what're": "what are",

                           "what's": "what is", "what've": "what have", "when's": "when is", "when've": "when have", "where'd": "where did", "where's": "where is",

                           "where've": "where have", "who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have",

                           "why's": "why is", "why've": "why have", "will've": "will have", "won't": "will not", "won't've": "will not have",

                           "would've": "would have", "wouldn't": "would not", "wouldn't've": "would not have", "y'all": "you all",

                           "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have",

                           "you'd": "you would", "you'd've": "you would have", "you'll": "you will", "you'll've": "you will have",

                           "you're": "you are", "you've": "you have"}

speaker_wise_dialogue_dict = {}
for i in unique_speakers:
  speaker_wise_dialogue_dict[i] = ""
speaker_wise_dialogue_dict

all_dialogues = test_df[test_df["raw_character_text"] == "Akira"]
all_dialogues

for i in unique_speakers:
  all_dialogues = []
  all_dialogues = test_df[test_df["raw_character_text"] == i]["spoken_words"]
  speaker_wise_dialogue_dict[i] = ' '.join(all_dialogues)
speaker_wise_dialogue_dict

#Cleaning text by updating the abbreviations
for i in unique_speakers:
  speaker_wise_dialogue_dict[i] = ' '.join([abbreviation_mapping[t] if t in abbreviation_mapping else t for t in speaker_wise_dialogue_dict[i].split(" ")]) 
speaker_wise_dialogue_dict

#Generating individual speaker summary
individual_speaker_summary = {}
for i in unique_speakers:
  individual_speaker_summary[i] = summarizer.summarize(speaker_wise_dialogue_dict[i], ratio = 0.5)
individual_speaker_summary

print(individual_speaker_summary['Akira']) #0.2 ratio

print(individual_speaker_summary['Akira']) #0.5 ratio