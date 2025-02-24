from app import app
from dash import Input, Output
from components.c_display_chart_group import create_display_chart_group


def serve_clb_update_layout_a(app):
    @app.callback(
        Output("output-layout", "children", allow_duplicate=True),
        Input("btn_output_selector_market_dynamics", "n_clicks"),
        Input("date_picker_time_horizon_training", "value"),
        Input("dropdown_country", "value"),
        prevent_initial_call=True,
    )
    def update_display_graphs1(n_clicks, dates, country):
        start_date_train = dates[0]
        finish_date_train = dates[1]
        return create_display_chart_group(country, start_date_train, finish_date_train)