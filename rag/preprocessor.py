import re
import unicodedata

def clean_text(text: str) -> str:
    """
    Cleans text based on specific requirements:
    - Convert to lowercase
    - Normalize unicode (NFKC)
    - Remove URLs
    - Remove HTML tags
    - Remove unnecessary special characters (keeps +, #, .)
    - Remove extra whitespaces
    """
    if not text:
        return ""

    # 1. Convert to lowercase
    text = text.lower()

    # 2. Normalize unicode (NFKC)
    text = unicodedata.normalize('NFKC', text)

    # 3. Remove URLs
    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    # 4. Remove HTML tags
    text = re.sub(r'<.*?>', '', text)

    # 5. Remove unnecessary special characters
    # We keep: alphanumerics, whitespace, and #, +, .
    # Note: we also keep standard punctuation like , ! ? for sentence structure
    # but the user said "remove unnecessary special characters (keep meaningful ones like +, #, .)"
    # We'll preserve basic sentence punctuation to "Preserve sentence structure" as requested.
    text = re.sub(r'[^a-z0-9\s+#.,!?]', '', text)

    # 6. Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text
