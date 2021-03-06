import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from utils import Header, make_dash_table
import pandas as pd


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Market Overview"], className="subtitle padded"
                                    ),
                                    html.Div([
                                        html.Div([
                                            html.Label('Market Capitalization'),

                                            dcc.Dropdown(id='market_cap', options=[
                                                {'label': 'Mega', 'value': 'mega'},
                                                {'label': 'Large', 'value': 'large'},
                                                {'label': 'Mid', 'value': 'mid'},
                                                {'label': 'Small', 'value': 'small'},
                                            ], value='mega'),

                                        ], className='three columns'),
                                        html.Div([
                                            html.Label('Sector'),
                                            dcc.Dropdown(id='sector', options=[
                                                {'label': 'Communications', 'value': 'communicationservices'},
                                                {'label': 'Consumer Cyclical', 'value': 'consumercyclical'},
                                                {'label': 'Consumer Defensive', 'value': 'consumerdefensive'},
                                                {'label': 'Technology', 'value': 'technology'},
                                                {'label': 'Financial', 'value': 'financial'},
                                                {'label': 'Real Estate', 'value': 'realestate'},
                                            ], value='communicationservices'),

                                        ], className='three columns'),
                                        html.Div([
                                            html.Label('Sort By'),

                                            dcc.Dropdown(id='sort_by', options=[
                                                {'label': 'Market Capitalization', 'value': 'marketcap'},
                                                {'label': 'Volume', 'value': 'volume'},
                                                {'label': 'Change', 'value': 'change'},
                                            ], value='marketcap'),

                                        ], className='three columns'),
                                        html.Button(['Stonks!'], id='update-market', style={'margin-left':'10px', 'margin-top': '15px'})


                                    ], className='row'),
                                    html.Table(id='market'),
                                ], className='tablemobile'
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
