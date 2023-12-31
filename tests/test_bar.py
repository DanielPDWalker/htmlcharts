import unittest
import os

from htmlcharts.bar import bar_chart
from pathlib import Path

class TestBar(unittest.TestCase):

    data = {"Mon": 4, "Tue": 2, "Wed": 8, "Thu": 1, "Fri": 0, "Sat": 3, "Sun": 2}

    def tearDown(self):
        if os.path.isfile(Path('html_chart.html')) and 1 == 2:
            os.remove(Path('html_chart.html'))

    def test_file_output_default(self):
        bar_chart(self.data, file_name="html_chart")
        self.assertFalse(os.path.isfile(Path('html_chart.html')))
    
    def test_file_output_true(self):
        bar_chart(self.data, file_output=True, file_name="html_chart")
        self.assertTrue(os.path.isfile(Path('html_chart.html')))  
