"""Bar chart"""

from math import floor
from htmlcharts.utils import max_bar_value


def bar_chart(data: dict, bar_height: int = 200, chart_width: int = 400, bar_color: str = "rgb(0,138,201)", label_color: str = "rgb(82,82,82)", file_output: bool = False, file_name: str = "html_chart"):

    #max_bar_value = max_bar_value(data)

    style = '''
        <style>
            .xaxis_labels {''' + f'''
                color: {label_color};''' + '''
                text-align: center;
                font-size: 16px;
                width: 14%;
                margin: 0;
                padding: 0;
            }
        </style>
    '''
    
    bar_values = []

    xaxis_html = ''

    for key, value in data.items():

        xaxis_html += f'<td class="xaxis_labels">{key}</td>'
        # use this list to get the max bar height
        bar_values.append(value)

    # get around divide by 0
    if max(bar_values) > 0:
        bar_height_multiplier = floor(bar_height / max(bar_values))
    else:
        bar_height_multiplier = 0

    bars_html = ''

    for key, value in data.items():

        set_bar_height = value * bar_height_multiplier

        # this is to fix 0 height still being 2px high and showing background color
        if value == 0:
            set_bar_color = "white"
            # this sets the bars to the max height always
            set_bar_height = bar_height
        else:
            set_bar_color = bar_color

        bars_html +=  f'''
            <td valign="bottom">
                <table style="width:100%;border-collapse:collapse">
                    <tbody>
                        <tr style="padding:0;">
                            <td height="{set_bar_height}" style="background-color: {set_bar_color};">
                            </td>
                        </tr>
                        <tr>
                            <td>
                                {value}
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        '''


    html = f'''
        <html>
            <head>
                {style}
            </head>
            <body>
                <table style="width: {chart_width};">
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
    '''

    if file_output:
        with open(f'{file_name}.html', 'w') as f:
            f.write(html)
    else:
        print(html)
