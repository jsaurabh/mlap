import string
from typing import List
import spacy as sp

spacy = sp.load("en_core_web_sm")

def lower(text: str) -> str:
    return text.lower()

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans("", "", string.punctuation))

def sanitize_ascii(text: str) -> str:
    return text.encode(encoding="ascii", errors="ignore").decode()

def tokenize(text: str) -> List[str]:
    return [token.text for token in spacy(text)]

text = ".string?with punc? Hej d\xe5"
ans = remove_punctuation(text)
print(ans, type(ans))

ans = sanitize_ascii(ans)
print(ans, type(ans))

ans = tokenize(ans)
print(ans, type(ans))