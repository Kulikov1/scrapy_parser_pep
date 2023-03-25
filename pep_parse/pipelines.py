from datetime import datetime as dt

from .constants import BASE_DIR, PEPS_COUNT


class PepParsePipeline:

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        PEPS_COUNT[item['status']] += 1
        return item

    def close_spider(self, spider):
        """При закрытии паука создает файл с общим кол-вом статусов"""
        total = sum(PEPS_COUNT.values())
        results_dir = BASE_DIR / 'results'
        file_name = f'status_summary_{dt.now():%Y-%m-%d_%H-%M-%S}.csv'
        file_path = results_dir / file_name
        with open(file_path, mode='w', encoding='utf-8') as f:
            f.write('Статус,Количество\n')
            for key, value in PEPS_COUNT.items():
                f.write(f'{key},{value}\n')
            f.write(f'Total,{total}\n')
