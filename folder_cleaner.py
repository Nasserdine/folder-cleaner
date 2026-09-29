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


def organize(folder, dry_run=False):
    folder = Path(folder).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Invalid directory: {folder}")

    moved = 0

    for file in folder.iterdir():
        if not file.is_file():
            continue

        category = get_category(file.suffix)
        destination = folder / category
        target = destination / file.name

        if target.exists():
            print(f"Skipped: {file.name} (already exists)")
            continue

        if dry_run:
            print(f"Would move: {file.name} -> {category}/")
        else:
            destination.mkdir(exist_ok=True)
            shutil.move(str(file), str(target))
            print(f"Moved: {file.name} -> {category}/")

        moved += 1

    if dry_run:
        print(f"\nDry run complete. {moved} file(s) would be organized.")
    else:
        print(f"\nDone. {moved} file(s) organized.")


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python folder_cleaner.py <folder> [--dry-run]")
        sys.exit(1)

    folder = sys.argv[1]
    dry_run = len(sys.argv) == 3 and sys.argv[2] == "--dry-run"

    if len(sys.argv) == 3 and sys.argv[2] != "--dry-run":
        print("Error: unknown option")
        print("Usage: python folder_cleaner.py <folder> [--dry-run]")
        sys.exit(1)

    try:
        organize(folder, dry_run=dry_run)
    except ValueError as error:
        print(f"Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
