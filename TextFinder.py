import argparse
import re

def find_word_in_file(word, file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the file content
            content = file.read()
            
        # Remove common punctuation and split into words
        words = re.findall(r'\b\w+\b', content.lower())
        
        # Count occurrences of the word in the cleaned content
        word_count = words.count(word.lower())
        
        print(f"The word '{word}' occurs {word_count} times in the file '{file_path}'.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Find occurrences of a word in a text file.")
    parser.add_argument("word", help="The word to search for")
    parser.add_argument("file", help="The path to the text file")

    # Parse arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    find_word_in_file(args.word, args.file)

