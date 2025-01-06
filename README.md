# Overview
The Sinhala Spelling and Grammar Correction Project is designed to address common errors in the Sinhala language, such as spelling mistakes and grammar issues. The project uses different approaches, including rule-based models and Levenshtein distance for spell checking, and aims to provide intelligent suggestions for improving the quality of Sinhala text.

# Features
Spell correction using a rule-based approach and dictionary comparison.

Grammar suggestions for better sentence structure.

Ability to suggest similar words using difflib for spell correction.

Levenshtein distance-based spell checker for intelligent suggestions.

Evaluation of model accuracy by comparing corrected text with predefined ground truth.


# Technologies Used
Python

difflib (for finding close matches)

Levenshtein distance algorithm

Jupyter Notebooks for implementation and testing

# Installation
## Clone the Repository
git clone https://github.com/<your-username>/sinhala-spell-correction.git
cd sinhala-spell-correction

## Install Dependencies
pip install -r requirements.txt

## Requirements
Python 3.x

Install dependencies using:
pip install difflib Levenshtein

# Usage
## Rule-Based Model for Spell Checking
The rule-based spell checker uses a predefined dictionary to check for spelling mistakes and suggest corrections.
![image](https://github.com/user-attachments/assets/40242027-ba71-4dea-a553-45a82a761e22)
![image](https://github.com/user-attachments/assets/b228f091-115a-4a7f-ad83-ef031ac9a14d)
![image](https://github.com/user-attachments/assets/43b0fff0-bf25-4a5f-a9c4-1e174696ae02)

## Levenshtein Distance Model for spell checker
The Levenshtein distance model finds the closest matching word in the dictionary for any misspelled word in the text.
![image](https://github.com/user-attachments/assets/d13189bb-2622-4d84-a397-ff2aecc9f6d1)
![image](https://github.com/user-attachments/assets/41f6b64a-75a0-4dcb-a5c9-944797d7259f)

# Deployment
Using streamlit
![image](https://github.com/user-attachments/assets/c16b9930-5552-410b-bcc2-106562c2e4f8)
![image](https://github.com/user-attachments/assets/cceb2ad2-87f5-4b7d-b490-02b926a310ff)

# Testing Accuracy
### For the rule-based model:
![image](https://github.com/user-attachments/assets/fdfa97cc-1e70-420a-8c42-a264ae8b18cd)

### For the Levenshtein model:
![image](https://github.com/user-attachments/assets/4fbcea7e-93ce-47f6-8d62-fdabace1d89d)






