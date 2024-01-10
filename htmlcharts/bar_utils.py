"""Supporting bar chart functions"""


def get_max_bar_value(data: dict):
    bar_values = []

    for key, value in data.items():
        bar_values.append(value)

    return max(bar_values)


def style_html_template(label_color: str, bar_width_percentage: int):
    return (
        """
        <style>
            .xaxis_labels {"""
        + f"""
                color: {label_color};"""
        + """
                text-align: center;
                font-size: 16px;"""
        + f"""
                width: {bar_width_percentage}%;"""
        + """
                margin: 0;
                padding: 0;
                padding-top: 2px;
            }
        </style>
    """
    )


def xaxis_html_template(data: dict):
    xaxis_html = ""

    for key, value in data.items():
        xaxis_html += f'<td class="xaxis_labels">{key}</td>'

    return xaxis_html


def join_html_template(style_html, xaxis_html, bars_html, chart_width):
    return f"""
        <html>
            <head>
                {style_html}
            </head>
            <body>
                <table style="min-width: {chart_width}px;">
                    <tbody>
                        <tr class="bars">
                            {bars_html}
                        </tr>
                        <tr class="xaxis">
                            {xaxis_html}
                        </tr>
                    </tbody>
                </table>
            </body>
        </html>
    """


def bars_html_template(data, bar_height_multiplier, bar_height, bar_color):
    bars_html = ""

    for key, value in data.items():
        set_bar_height = value * bar_height_multiplier

        # this is to fix 0 height still being 2px high and showing background color
        if value == 0:
            set_bar_color = "white"
            # this sets the bars to the max height always
            set_bar_height = bar_height
        else:
            set_bar_color = bar_color

        bars_html += f"""
            <td valign="bottom">
                <table style="width:100%; border-collapse:collapse">
                    <tbody>
                        <tr style="padding:0;">
                            <td height="{set_bar_height}" style="background-color: {set_bar_color};">
                            </td>
                        </tr>
                        <tr>
                            <td style="font-size: 13px; text-align:center; padding-top: 5px;">
                                {value}
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        """

    return bars_html
