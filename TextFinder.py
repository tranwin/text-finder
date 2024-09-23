import argparse
import re
import PyPDF2

def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"An error occurred while reading the PDF: {e}")
        return None

def find_word_in_file(word, file_path):
    content = None

    # Check if file is PDF or TXT
    if file_path.endswith(".pdf"):
        content = extract_text_from_pdf(file_path)
    elif file_path.endswith(".txt"):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' does not exist.")
            return
    else:
        print(f"Error: Unsupported file type. Only '.txt' and '.pdf' are supported.")
        return

    if content:
        # Remove common punctuation and split into words
        words = re.findall(r'\b\w+\b', content.lower())
        
        # Count occurrences of the word in the cleaned content
        word_count = words.count(word.lower())
        
        print(f"The word '{word}' occurs {word_count} times in the file '{file_path}'.")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Find occurrences of a word in a text or PDF file.")
    parser.add_argument("word", help="The word to search for")
    parser.add_argument("file", help="The path to the text or PDF file")

    # Parse arguments
    args = parser.parse_args()

    # Call the function with the provided arguments
    find_word_in_file(args.word, args.file)


