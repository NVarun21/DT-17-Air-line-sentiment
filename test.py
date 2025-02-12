import re
import nltk
from nltk.tokenize import word_tokenize
nltk.download("punkt")
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer

class TextToNum:
    def __init__(self, text):
        self.text = text

    def cleaner(self):
        # Preserve important punctuation
        text = re.sub(r',', '', self.text)
        cleaned_text = re.sub(r'[^\w\s!?.]', '', text)  
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        self.cleaned = cleaned_text

    def token(self):
        self.tkns = word_tokenize(self.cleaned.lower())  # Convert to lowercase

    def removeStop(self):
        stop = set(stopwords.words('english'))
        negation_words = {"not", "no", "never", "n't", "don’t", "isn’t"}

        # Keep negation words, remove other stopwords
        self.cl = [word for word in self.tkns if word not in stop or word in negation_words]

    def stemme(self):
        ps = PorterStemmer()
        self.st = [ps.stem(word) for word in self.cl]
        return self.st