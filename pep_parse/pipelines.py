import csv
from datetime import datetime as dt

from .constants import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider) -> None:
        global peps_count
        peps_count = {
            'Total': 0,
        }

    def process_item(self, item, spider) -> object:
        status = item.get('status')
        if status not in peps_count:
            peps_count[status] = 0
        peps_count[status] += 1
        peps_count['Total'] += 1
        return item

    def close_spider(self, spider) -> None:
        """При закрытии паука создает файл с общим кол-вом статусов"""
        results_dir = BASE_DIR / 'results'
        file_name = f'status_summary_{dt.now():%Y-%m-%d_%H-%M-%S}.csv'
        file_path = results_dir / file_name
        with open(file_path, mode='w', newline='', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            fieldnames = peps_count.keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(peps_count)
