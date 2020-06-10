from django.shortcuts import render



# Create your views here.

from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

def chart_view(request):
    if request.method == 'POST':
    
        number = int(request.POST.get("number"))
    else:
        number = 2
    x_data = [0,1,2,3,4,5,6,7,8,9]
    y_data = [x**number for x in x_data]

    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
    return render(request, "charts.html", context={'plot_div': plot_div})









