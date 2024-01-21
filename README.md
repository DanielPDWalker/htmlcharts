# htmlcharts
Python package to create pure html and css charts. `htmlcharts` is designed to be used to create charts you can email, as most email providers will remove any `javascript` sent in an email by default.

Results will still vary by email service provider. (Some support ways of using `CSS` that other don't for example).

**Status: In Development**

---

# Usage

## Installation

Install the package to your project/python environment
`pip install git+https://github.com/DanielPDWalker/htmlcharts.git`

Pin to a release version for stability by adding `@vx.x.x` to the end of the above command

## Creating a chart

Import the `bar_chart` function

`from htmlcharts.bar import bar_chart`


Call the function and pass in your chart data.
```
chart_data_dict = {"Mon": 4, "Tue": 3, "Wed": 7, "Thu": 2, "Fri": 6, "Sat": 3, "Sun": 4}

bar_chart_html = bar_chart(chart_data_dict)
```

### Chart Data

The format for chart data is a python dictionary with `string` keys, and `int` values.

### Function Settings

| **Function Settings**           | **Format** | **Default** | **Description** |
| ------------------------------- | ---------- | ----------- | --------------- |
| `data` | `dict` | `None` | `dict` of `string` keys and `int` values |
| `bar_height` | `int` | `200` | Sets max height of bars in chart. (Not overall canvas height, just bar height) |
| `chart_width` | `int` | `400` | Sets chart width |
| `bar_color` | `string` | `rgb(0,138,201)` | Sets the color of the chart bars. Any color string that works in css |
| `label_color` | `string` | `rgb(82,82,82)` | Sets the font color for the xaxis labels. Any color string that works in css |
| `file_output` | `boolean` | `False` | Enable output of html file containing the chart |
| `file_name` | `string` | `html_chart` | Name for the output file |
