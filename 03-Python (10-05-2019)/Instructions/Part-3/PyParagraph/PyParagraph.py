# -*- coding: UTF-8 -*-
"""PyParagraph Homework Solution."""

# Incorporate regular expressions (helpful for splitting by punctuation)
import re
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("raw_data", "paragraph_1.txt")
file_to_output = os.path.join("analysis", "paragraph_analysis.txt")

# String variable to hold the paragraph contents
paragraph = ""

# Read the text file
with open(file_to_load) as txt_data:

    # Store the contents as a string (with no new lines)
    paragraph = txt_data.read().replace("\n", " ")
# Split the paragraph based on spaces to calculate word count
word_split = paragraph.split(" ")
word_count = len(word_split)

# Create a list for holding all the letter counts
letter_counts = []

# Loop through the word array and calculate the length of each word
for word in word_split:

    # Add each letter count into the letter_counts list
    letter_counts.append(len(word))

# Calculate the avg letter count
avg_letter_count = sum(letter_counts) / float(len(letter_counts))

# Re-split the original paragraph based on punctuation (. ? !)
sentence_split = re.split("(?<=[.!?]) +", paragraph)
sentence_count = len(sentence_split)
words_per_sentence = []

# Loop through the sentence array and calculate the number of words in each
#for sentence in sentence_split:
for sentence in sentence_split:
    

    # Calculate the number of words in each sentence and add to the list
    #YOUR CODE HERE
    sentence = sentence.split(" ")
    words_per_sentence.append(len(sentence))
    
# Calculate the avg word count (per sentence)
#YOUR CODE HERE
print(words_per_sentence)
avg_wps_count = sum(words_per_sentence) / float(len(words_per_sentence))

# Generate Paragraph Analysis Output
#YOUR CODE HERE
printable_wc = f'Approximate Word Count: {word_count}\n'
printable_sc = f'Approximate Sentence Count: {sentence_count}\n'
printable_alc = f'Average Letter Count: {avg_letter_count}\n'
printable_asl = f'Average Sentence Length: {avg_wps_count}\n'

# Print all of the results (to terminal)
#YOUR CODE HERE
header = print("Paragraph Analysis")
seperator = print("-----------------")
print(printable_wc + printable_sc + printable_alc + printable_asl)

# Save the results to analysis text file
#YOUR CODE HERE
file = open("paragraph_analysis.txt","w") 

file.write(str("Paragraph Analysis\n"))
file.write(str("-----------------\n"))
file.write(str(printable_wc))
file.write(str(printable_sc))
file.write(str(printable_alc))
file.write(str(printable_asl))   

file.close() 