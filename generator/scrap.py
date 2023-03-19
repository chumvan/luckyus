from typing import Dict
import requests
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words

BASE_URL = "https://eonet.gsfc.nasa.gov/api/v3"


def report_latest_event() -> str:
    s = "Latest event: "
    resp = requests.get(BASE_URL + "/events" + "?limit=1")
    s += resp.json()["events"][0]["title"] + "\n"
    link = resp.json()["events"][0]["sources"][0]["url"]
    parser = HtmlParser.from_url(link, Tokenizer("english"))
    stemmer = Stemmer("english")
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words("english")
    for sentence in summarizer(parser.document, 5):
        s += str(sentence)
    return s
