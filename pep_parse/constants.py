import re
from pathlib import Path

ALLOWED_DOMAINS = 'peps.python.org'

START_URLS = 'https://peps.python.org/'

# Ищет номер и название пеп
PATERN = re.compile(r'(?P<number>\d*) – (?P<name>.*)')

BASE_DIR = Path(__file__).parent.parent
