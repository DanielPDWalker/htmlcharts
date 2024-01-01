"""Bar chart"""

from math import floor
from htmlcharts.bar_utils import *


def bar_chart(
    data: dict,
    bar_height: int = 200,
    chart_width: int = 400,
    bar_color: str = "rgb(0,138,201)",
    label_color: str = "rgb(82,82,82)",
    file_output: bool = False,
    file_name: str = "html_chart",
):
    max_bar_value = get_max_bar_value(data)

    style_html = style_html_template(label_color)

    xaxis_html = xaxis_html_template(data)

    if max_bar_value > 0:
        bar_height_multiplier = floor(bar_height / max_bar_value)
    else:
        bar_height_multiplier = 0

    bars_html = bars_html_template(data, bar_height_multiplier, bar_height, bar_color)

    joined_html = join_html_template(style_html, xaxis_html, bars_html, chart_width)

    if file_output:
        with open(f"{file_name}.html", "w") as f:
            f.write(joined_html)
    else:
        return(joined_html)
