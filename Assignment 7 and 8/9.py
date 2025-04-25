# 9. Create a tokenizer for your own language (mother tongue you speak). The tokenizer should
# tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,

# “3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
# this. [Hint: Use unicode blocks for your language, check wikipedia pages]
import re

# Define regex patterns for each component
patterns = {
    "punctuation": r'[.,!?;:(){}[\]<>|\\/-]',     
    "date": r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b',  
    "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',  
    "number": r'\b(\d{1,3}(?:,\d{3})*|\d+\.\d+|\d+)\b',  
    "social_media_handle": r'@\w+',  
    "unicode_language": r'[\u0900-\u097F]+',   
}

# Combine all patterns into one big pattern
combined_pattern = "|".join(f"(?P<{key}>{pattern})" for key, pattern in patterns.items())

# Function to tokenize text
def tokenize(text):
    tokens = []
    for match in re.finditer(combined_pattern, text):
        for key, group in match.groupdict().items():
            if group:  # If the group matched something
                tokens.append((key, group))
    return tokens

text = "Hey @user123! Please visit https://example.com or email me at test@example.com. " \
       "The event is on 12/12/2025, and the number is 33,123.50."

tokens = tokenize(text)

for token in tokens:
    print(token)
