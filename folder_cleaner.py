from pathlib import Path
import shutil
import sys

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".odt"},
    "Spreadsheets": {".xls", ".xlsx", ".csv", ".ods"},
    "Presentations": {".ppt", ".pptx", ".odp"},
    "Videos": {".mp4", ".mov", ".avi", ".mkv"},
    "Audio": {".mp3", ".wav", ".flac", ".aac"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
}


def get_category(extension):
    extension = extension.lower()

    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"


def organize(folder):
    folder = Path(folder).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Invalid directory: {folder}")

    moved = 0

    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = get_category(file.suffix)
        destination = folder / category
        destination.mkdir(exist_ok=True)

        target = destination / file.name

        if target.exists():
            print(f"Skipped: {file.name} (already exists)")
            continue

        shutil.move(str(file), str(target))
        print(f"Moved: {file.name} -> {category}/")
        moved += 1

    print(f"\nDone. {moved} file(s) organized.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python folder_cleaner.py <folder>")
        sys.exit(1)

    try:
        organize(sys.argv[1])
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)
