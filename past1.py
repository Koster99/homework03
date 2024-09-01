import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def copy_file_to_target(file_path, target_dir):
    """
    Копіює файл до цільової директорії, яка відповідає його розширенню.
    """
    extension = file_path.suffix[1:]  # Отримуємо розширення без крапки
    target_path = target_dir / extension / file_path.name
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(file_path, target_path)

def process_directory(source_dir, target_dir):
    """
    Рекурсивно обходить всі піддиректорії та файли в заданій директорії.
    """
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(source_dir):
            root_path = Path(root)
            for file in files:
                file_path = root_path / file
                executor.submit(copy_file_to_target, file_path, target_dir)

if __name__ == "__main__":
    import sys

    # Отримання шляхів до директорій із аргументів командного рядка
    source_dir = Path(sys.argv[1])
    target_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    process_directory(source_dir, target_dir)
