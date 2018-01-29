import unittest
import os.path as path

def to_html (file_name):
    file_name, _ = path.splitext(file_name)
    return file_name + '.html'


class PythonScriptToHtml(unittest.TestCase):

    def test_absolute_name(self):
        self.assertEqual(to_html('/usr/local/share/index.py'), '/usr/local/share/index.html')

if __name__ == '__main__':
    unittest.main()