import unittest
import os

from htmlcharts.bar import bar_chart
from pathlib import Path


class TestBar(unittest.TestCase):
    data = {"Mon": 4, "Tue": 2, "Wed": 10, "Thu": 1, "Fri": 0, "Sat": 3, "Sun": 2}

    def tearDown(self):
        if os.path.isfile(Path("html_chart.html")):
            os.remove(Path("html_chart.html"))

    def test_file_output_default(self):
        bar_chart_html = bar_chart(self.data)
        self.assertFalse(os.path.isfile(Path("html_chart.html")))
        self.assertTrue(bar_chart_html != None)

    def test_file_output_true(self):
        bar_chart_html = bar_chart(self.data, file_output=True)
        self.assertTrue(os.path.isfile(Path("html_chart.html")))
        self.assertTrue(bar_chart_html == None)

    def test_bar_height_default_value(self):
        bar_chart_html = bar_chart(self.data)
        self.assertTrue('height="200"' in bar_chart_html)

    def test_bar_height_custom_value(self):
        custom_data = {
            "Mon": 0,
            "Tue": 0,
            "Wed": 10,
            "Thu": 0,
            "Fri": 0,
            "Sat": 0,
            "Sun": 0,
        }
        bar_chart_html = bar_chart(custom_data, bar_height=500)
        self.assertFalse('height="200"' in bar_chart_html)
        self.assertTrue('height="500"' in bar_chart_html)

    def test_default_chart_width(self):
        bar_chart_html = bar_chart(self.data)
        self.assertTrue('table style="width: 400;"' in bar_chart_html)

    def test_custom_chart_width(self):
        bar_chart_html = bar_chart(self.data, chart_width=800)
        self.assertFalse('table style="width: 400;"' in bar_chart_html)
        self.assertTrue('table style="width: 800;"' in bar_chart_html)

    def test_default_bar_color(self):
        bar_chart_html = bar_chart(self.data)
        self.assertTrue('style="background-color: rgb(0,138,201);"' in bar_chart_html)

    def test_custom_bar_color(self):
        bar_chart_html = bar_chart(self.data, bar_color="rgb(255,0,0)")
        self.assertFalse('style="background-color: rgb(0,138,201);"' in bar_chart_html)
        self.assertTrue('style="background-color: rgb(255,0,0);"' in bar_chart_html)
