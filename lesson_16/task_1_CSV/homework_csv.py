import csv
from pathlib import Path


def merge_csv_remove_duplicates(surname: str) -> Path:
    source_folder = Path("lesson_16/task_1_CSV/work_with_csv")
    result_folder = Path("lesson_16/task_1_CSV")
    csv_files = sorted(source_folder.glob("*.csv"))[:2]

    if len(csv_files) < 2:
        raise FileNotFoundError(f"Нужно минимум 2 CSV в {source_folder}, найдено: {len(csv_files)}")

    header = None
    rows = set()

    for file in csv_files:
        with open(file, newline="", encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f)
            try:
                h = next(reader)
            except StopIteration:
                continue
            if header is None:
                header = h
            for row in reader:
                rows.add(tuple(row))
    if header is None:
        raise ValueError("Не удалось прочитать файлы")
    result_file = result_folder / f"result_{surname}.csv"

    with open(result_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(sorted(rows))

    return result_file


if __name__ == "__main__":
    out = merge_csv_remove_duplicates("Isai")
    print("Все готово:", out)