import json
import logging
from pathlib import Path


def validate_json_files(surname: str) -> Path:
    folder = Path("lesson_16/task_2_JSON/work_with_json")
    log_path = Path("lesson_16/task_2_JSON") / f"json__{surname}.log"

    logger = logging.getLogger("json_validator")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setLevel(logging.ERROR)
    file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(file_handler)

    json_files = [p for p in folder.iterdir() if p.is_file()]
    if not json_files:
        raise FileNotFoundError(f"В папке {folder} нет файлов")
    for file in sorted(json_files):
        try:
            with open(file, "r", encoding="utf-8") as f:
                json.load(f)
        except Exception as e:
            logger.error("Невалидный JSON: %s | %s", file.name, repr(e))
    return log_path


if __name__ == "__main__":
    log_file = validate_json_files("Isai")  # ← фамилия
    print("Проверка завершена. Лог:", log_file)
