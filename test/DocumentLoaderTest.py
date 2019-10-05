import unittest

from test.MockFS import generate_mock_folder
from src.DocumentLoader import DocumentLoader
from os import path


class DocumentLoaderTest(unittest.TestCase):
	def test_data_collection(self):
		generate_mock_folder()
		mock_dir = path.join(path.dirname(__file__), "mock")
		loader = DocumentLoader(mock_dir)
		loader.load_text_files()
		self.assertTrue(path.join(mock_dir, "a.txt") in loader.files)
		self.assertTrue(path.join(mock_dir, "b.txt") in loader.files)
		self.assertTrue(path.join(mock_dir, "c.ab.txt") in loader.files)


if __name__ == '__main__':
	unittest.main()