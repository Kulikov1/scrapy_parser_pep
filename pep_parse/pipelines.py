import csv
from datetime import datetime as dt

from .constants import BASE_DIR


class PepParsePipeline:
    def __init__(self):
        self.peps_count = {
            'Total': 0,
        }

    def open_spider(self, spider) -> None:
        pass

    def process_item(self, item, spider) -> object:
        status = item.get('status')
        if status not in self.peps_count:
            self.peps_count[status] = 0
        self.peps_count[status] += 1
        self.peps_count['Total'] += 1
        return item

    def close_spider(self, spider) -> None:
        """При закрытии паука создает файл с общим кол-вом статусов"""
        results_dir = BASE_DIR / 'results'
        file_name = f'status_summary_{dt.now():%Y-%m-%d_%H-%M-%S}.csv'
        file_path = results_dir / file_name
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            fieldnames = self.peps_count.keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(self.peps_count)
