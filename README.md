# Folder Cleaner

A simple Python command-line tool that automatically organizes files into folders based on their file type.

## Features

- Automatically organizes files by type
- Supports images, documents, spreadsheets, presentations, videos, audio and archives
- Creates folders automatically
- Prevents accidental overwriting of existing files
- Works on Windows, macOS and Linux

## Requirements

- Python 3.9 or newer

## Usage

Clone the repository:

```bash
git clone https://github.com/Nasserdine/folder-cleaner.git
cd folder-cleaner
```

Run the tool:

```bash
python folder_cleaner.py ~/Downloads
```

Replace `~/Downloads` with the folder you want to organize.

## Categories

Files are organized into:

- Images
- Documents
- Spreadsheets
- Presentations
- Videos
- Audio
- Archives
- Other

## Example

Before:

```text
Downloads/
├── photo.jpg
├── report.pdf
├── music.mp3
└── archive.zip
```

After:

```text
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── music.mp3
└── Archives/
    └── archive.zip
```

## License

This project is licensed under the MIT License.
