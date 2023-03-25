import re
from pathlib import Path

# Ищет номер и название пеп
PATERN = re.compile(r'(?P<number>\d*) – (?P<name>.*)')

BASE_DIR = Path(__file__).parent.parent

PEPS_COUNT = {
    'Active': 0,
    'Accepted': 0,
    'Deferred': 0,
    'Final': 0,
    'Provisional': 0,
    'Rejected': 0,
    'Superseded': 0,
    'Withdrawn': 0,
    'April Fool!': 0,
    'Draft': 0,
}
