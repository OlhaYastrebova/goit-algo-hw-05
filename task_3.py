import re
import sys
from pathlib import Path
from typing import Callable, List, Dict

def parse_log_line(line: str) -> Dict:
    """Парсинг рядка логу."""
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)', line)
    if match:
        return {
            'datetime': match.group(1),
            'level': match.group(2),
            'message': match.group(3)
        }
    return {}

def load_logs(file_path: str) -> List[Dict]:
    """Завантаження логів з файлу."""
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
    return logs

def filter_logs_by_level(logs: List[Dict], level: str) -> List[Dict]:
    """Фільтрація логів за рівнем."""
    return [log for log in logs if log['level'].upper() == level.upper()]

def count_logs_by_level(logs: List[Dict]) -> Dict[str, int]:
    """Підрахунок записів за рівнем логування."""
    counts = {}
    for log in logs:
        level = log['level']
        counts[level] = counts.get(level, 0) + 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """Форматування та вивід результатів."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in sorted(counts.items()):
        print(f"{level.ljust(15)} | {count}")

def display_filtered_logs(logs: List[Dict], level: str):
    """Вивід логів для певного рівня."""
    print(f"\nДеталі логів для рівня '{level.upper()}':")
    for log in logs:
        print(f"{log['datetime']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Використання: python task_3.py logfile.log [level]")
        return

    script_path = Path(__file__).resolve()
    script_dir = script_path.parent
    file_path = script_dir / sys.argv[1]
    level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    if not logs:
        print("Логи не знайдені або файл порожній.")
        return

    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        display_filtered_logs(filtered_logs, level)

if __name__ == "__main__":
    main()
