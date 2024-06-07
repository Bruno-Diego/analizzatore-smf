# import plotly.express as px
import plotly.graph_objects as go
from django.shortcuts import render
import pandas as pd

def drawChartExec(df, medie_df):

    # # Bar Chart
    # wide_df = px.data.medals_wide()

    # fig_bar = px.bar(wide_df, x="nation", y=["gold", "silver", "bronze"], title="Wide-Form Input", height=300)

    # # Scatter Chart
    # df = px.data.iris()
    # fig_scatter = px.scatter(df, x="sepal_width", y="sepal_length", color="species", height=300, hover_data=['petal_width'])

    # Line Chart
    # df = px.data.gapminder().query("country in ['Canada', 'Botswana']")
    # df = px.data.gapminder().query("country in ['Canada', 'Botswana']")
    
    filtered_df = df[df['SMF123S2_API_REQ_NAME'].isin([medie_df['SMF123S2_API_REQ_NAME']])]

    # print(medie_df)

    # fig_line = px.line(medie_df, x="Num. Esecuzioni", y="SMF123S2_API_REQ_NAME", height=600)
    # fig_line.update_traces(textposition="bottom right")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=medie_df["Num. Esecuzioni"], 
        y=medie_df['SMF123S2_API_REQ_NAME'],
        mode='markers', 
        name='markers', 
        textposition="bottom right"))
    
    # # Pie Chart
    # df = px.data.tips()
    # fig_pie = px.pie(df, values='tip', names='day', height=300)


    # bar_chart = fig_bar.to_html(full_html=False, include_plotlyjs=False)
    # scatter_chart = fig_scatter.to_html(full_html=True, include_plotlyjs=False)
    
    # line_chart = fig_line.to_html(full_html=False, include_plotlyjs=False)
    fig.update_layout(
        autosize=False,
        width=700,
        height=700,
        hovermode='y',
        # yaxis=dict(
        #     title_text="Y-axis Title",
        #     ticktext=["Very long label", "long label", "3", "label"],
        #     tickvals=[1, 2, 3, 4],
        #     tickmode="array",
        #     titlefont=dict(size=30),
        # )
    )
    # fig.add_trace(go.Scatter(
    #     mode="markers", 
    #     textposition="bottom right"
    #     )
    # )
    line_chart = fig.to_html(full_html=False, include_plotlyjs=False)
    
    # pie_chart = fig_pie.to_html(full_html=False, include_plotlyjs=False)
    
    # return render(request, "plotly.html", {"bar_chart": bar_chart ,
    #                                        "scatter_chart" : scatter_chart, 
    #                                        "line_chart" : line_chart, 
    #                                        "pie_chart": pie_chart})
    return line_chart
    # return fig.show()

def drawChartTempo(df, medie_df):

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=medie_df["Tempo Medio Esecuzione"], 
        y=medie_df['SMF123S2_API_REQ_NAME'],
        mode='markers', 
        name='markers',
        textposition="bottom right"
        )
    )
    fig.update_layout(
        autosize=False,
        width=700,
        height=700,
        hovermode='y',
    )
    line_chart = fig.to_html(full_html=False, include_plotlyjs=False)
    return line_chart
    