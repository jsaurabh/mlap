import re

def count_syllables(text: str) -> int:
    ### https://codereview.stackexchange.com/a/224180
    return len(
        re.findall('(?!e$)[aeiouy]+', text, re.I) +
        re.findall('^[^aeiouy]*e$', text, re.I)
    )

def count_words(text: str) -> int:
    return len(re.findall(r'\w+', text))

def count_sentences(text: str) -> int:
    return len(re.split(r'.+', text))

def flesch_score(text: str) -> float:
    total_syllables = count_syllables(text)
    total_words = count_words(text)
    total_sentences = count_sentences(text)

    return 206.835 - 1.015 * float(total_words)/total_sentences \
        - 84.6 * (float(total_syllables)/total_words)

score = flesch_score("HAIRY IS MY NAME. What do you want.")
print(score)