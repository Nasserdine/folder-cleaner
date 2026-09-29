import tempfile
import unittest
from pathlib import Path

from folder_cleaner import get_category, organize


class TestFolderCleaner(unittest.TestCase):

    def test_image_category(self):
        self.assertEqual(get_category(".jpg"), "Images")
        self.assertEqual(get_category(".PNG"), "Images")

    def test_document_category(self):
        self.assertEqual(get_category(".pdf"), "Documents")
        self.assertEqual(get_category(".txt"), "Documents")

    def test_unknown_category(self):
        self.assertEqual(get_category(".xyz"), "Other")

    def test_organize_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            folder = Path(temp_dir)

            (folder / "photo.jpg").write_text("test")
            (folder / "document.pdf").write_text("test")
            (folder / "archive.zip").write_text("test")

            organize(folder)

            self.assertTrue(
                (folder / "Images" / "photo.jpg").exists()
            )
            self.assertTrue(
                (folder / "Documents" / "document.pdf").exists()
            )
            self.assertTrue(
                (folder / "Archives" / "archive.zip").exists()
            )


if __name__ == "__main__":
    unittest.main()
