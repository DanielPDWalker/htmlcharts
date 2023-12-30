import unittest
import os

from htmlcharts.bar import bar_chart
from pathlib import Path

class TestBar(unittest.TestCase):
    
    data = {"Mon": 4, "Tue": 2, "Wed": 8, "Thu": 1, "Fri": 0, "Sat": 3, "Sun": 2}
    
    def test_file_output(self):
        bar_chart(self.data, file_output=True, file_name="html_chart")
        self.assertTrue(os.path.isfile(Path('html_chart.html')))


