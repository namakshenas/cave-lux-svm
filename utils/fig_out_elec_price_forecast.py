import plotly.express as px
import pandas as pd
from controls.cl_fig_update_layout import create_update_layout_fig
import os


def serve_fig_out_elec_price_forecast(freq):
    df = pd.read_csv(
        os.path.join(os.path.dirname('./data/'), 'elec_price_forecast.csv'),
        delimiter=';'
    )

    df['date'] = pd.to_datetime(df['date'])

    # start_date_train = "2024-01-01"
    # finish_date_train = "2025-01-01"
    #
    # df = df.loc[(df['date'] > start_date_train) & (df['date'] <= finish_date_train)]

    df = df.groupby(pd.Grouper(key="date", freq=freq)).mean()
    df = df.reset_index()

    fig = px.line(df, x='date', y="value", )

    create_update_layout_fig(fig, "Forecasted electricity forward curve")
    # fig.update_traces(fillcolor="rgba(204,204,255,.15)")

    fig.update_yaxes(
        range=[min(df["value"]) - 2, max(df["value"]) + 2],
    )
    # fig.update_xaxes(
    #     rangeslider_visible=True,
    #     # rangeselector=dict(
    #     #     buttons=list([
    #     #         dict(count=1, label="1m", step="day", stepmode="backward"),
    #     #         dict(count=6, label="6m", step="month", stepmode="backward"),
    #     #         dict(count=1, label="YTD", step="year", stepmode="todate"),
    #     #         dict(count=1, label="1y", step="year", stepmode="backward"),
    #     #         dict(step="all")
    #     #     ])
    #     # )
    # )

    return fig
