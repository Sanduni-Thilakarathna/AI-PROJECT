
import re
import difflib
import streamlit as st

class SinhalaSpellChecker:
    def __init__(self):
        self.word_set = set()  # Using a set for fast lookup

    def train_from_txt(self, txt_path):
        try:
            with open(txt_path, 'r', encoding='utf-8') as file:
                text = file.read()
                self.train(text)
            return f"Successfully trained using {txt_path}", len(self.word_set)
        except FileNotFoundError:
            return f"Error: File {txt_path} not found", 0
        except UnicodeDecodeError:
            return f"Error: File {txt_path} is not properly encoded. Please ensure it's saved as UTF-8", 0

    def train(self, text):
        text = self._normalize_text(text)
        words = text.split()
        self.word_set.update(words)

    def _normalize_text(self, text):
    # Remove punctuation and extra spaces
      #text = re.sub(r'(.,!?[]'"", text)  # Corrected punctuation removal
      text = text.strip()  # Remove leading/trailing spaces
      text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
      return text




    def check_word(self, word):
        if word in self.word_set:
            return True  # Word is correct
        else:
            # Use Levenshtein distance to find closest matching word in the dictionary
            closest_match = self._find_closest_match(word)
            if closest_match:
                return f"Did you mean '{closest_match}'?", False
            return None, False  # Word is incorrect

    def _find_closest_match(self, word):
        closest_match = difflib.get_close_matches(word, self.word_set, n=3, cutoff=0.6)
        if closest_match:
            return closest_match[0]  # Suggest the closest match
        return None

    def check_manually_entered_text(self, text):
        words = self._normalize_text(text).split()

        incorrect_words = []
        suggestions = []

        for word in words:
            result = self.check_word(word)  # Get result from check_word
            
            if result:  # If result is not None
                if isinstance(result, tuple):  # Check if result is a tuple
                    suggestion, correct = result  # Unpack suggestion and correctness
                    if not correct:
                        incorrect_words.append(word)
                        if suggestion:
                            suggestions.append(suggestion)
                else:
                    # Handle case where result is not a tuple (shouldn't happen)
                    incorrect_words.append(word)
                    suggestions.append("No suggestion available")

        if incorrect_words:
            return incorrect_words, suggestions
        else:
            return None, None

# Streamlit UI
def main():
    # Create Streamlit title and description
    st.title("Sinhala Spell Checker")
    st.markdown("This is a Sinhala spell checker. It will check the spelling of words from a Sinhala text file and suggest corrections.")

    # Upload the training TXT file
    uploaded_file = st.file_uploader("Upload the Sinhala text file for training", type=["txt"])

    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with open("/tmp/uploaded_file.txt", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Initialize spell checker
        checker = SinhalaSpellChecker()

        # Train from the uploaded file
        status, num_words = checker.train_from_txt("/tmp/uploaded_file.txt")
        st.write(status)
        st.write(f"Learned {num_words} unique words.")

        # Text input area for checking spelling
        user_input = st.text_area("Enter Sinhala text to check spelling")

        if st.button("Check Spelling"):
            if user_input:
                incorrect_words, suggestions = checker.check_manually_entered_text(user_input)

                if incorrect_words:
                    st.subheader("Incorrect words found:")
                    for word, suggestion in zip(incorrect_words, suggestions):
                        st.write(f"'{word}' is incorrect. {suggestion}")
                else:
                    st.write("All words are correct.")
            else:
                st.write("Please enter a sentence to check.")

if __name__ == "__main__":
    main()

