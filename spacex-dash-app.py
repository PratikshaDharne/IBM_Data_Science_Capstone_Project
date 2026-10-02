
import pandas as pd
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# --------------------------------------------------
# 1. Load SpaceX dataset
# --------------------------------------------------

spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Get minimum and maximum payload values
min_payload = spacex_df["Payload Mass (kg)"].min()
max_payload = spacex_df["Payload Mass (kg)"].max()

# Get unique launch sites
launch_sites = spacex_df["Launch Site"].unique()

# --------------------------------------------------
# 2. Initialize Dash application
# --------------------------------------------------

app = dash.Dash(__name__)

# --------------------------------------------------
# 3. Create dashboard layout
# --------------------------------------------------

app.layout = html.Div(
    children=[

        html.H1(
            "SpaceX Launch Records Dashboard",
            style={
                "textAlign": "center",
                "color": "#503D36",
                "fontSize": 40
            }
        ),

        # TASK 1: Launch Site Dropdown

        html.Div([
            html.Label("Select Launch Site:"),

            dcc.Dropdown(
                id="site-dropdown",
                options=[
                    {"label": "All Sites", "value": "ALL"}
                ] + [
                    {"label": site, "value": site}
                    for site in launch_sites
                ],
                value="ALL",
                placeholder="Select a Launch Site here",
                searchable=True
            )
        ]),

        html.Br(),

        # TASK 2: Success Pie Chart

        html.Div(
            dcc.Graph(id="success-pie-chart")
        ),

        html.Br(),

        # TASK 3: Payload Range Slider

        html.Div([
            html.Label("Select Payload Range (Kg):"),

            dcc.RangeSlider(
                id="payload-slider",
                min=0,
                max=10000,
                step=1000,
                marks={
                    0: "0",
                    2000: "2000",
                    4000: "4000",
                    6000: "6000",
                    8000: "8000",
                    10000: "10000"
                },
                value=[min_payload, max_payload]
            )
        ]),

        html.Br(),

        # TASK 4: Payload Scatter Chart

        html.Div(
            dcc.Graph(id="success-payload-scatter-chart")
        )
    ]
)

# --------------------------------------------------
# TASK 2: Callback for Success Pie Chart
# --------------------------------------------------

@app.callback(
    Output(
        component_id="success-pie-chart",
        component_property="figure"
    ),
    Input(
        component_id="site-dropdown",
        component_property="value"
    )
)

def get_pie_chart(entered_site):

    if entered_site == "ALL":

        # Count successful launches for each launch site
        success_df = spacex_df[
            spacex_df["class"] == 1
        ]

        fig = px.pie(
            success_df,
            names="Launch Site",
            title="Total Successful Launches by Site"
        )

    else:

        # Filter data for selected launch site
        filtered_df = spacex_df[
            spacex_df["Launch Site"] == entered_site
        ]

        # Count successful and failed launches
        fig = px.pie(
            filtered_df,
            names="class",
            title=f"Launch Outcomes for {entered_site}",
            labels={
                "class": "Launch Outcome"
            }
        )

    return fig


# --------------------------------------------------
# TASK 4: Callback for Payload Scatter Chart
# --------------------------------------------------

@app.callback(
    Output(
        component_id="success-payload-scatter-chart",
        component_property="figure"
    ),
    [
        Input(
            component_id="site-dropdown",
            component_property="value"
        ),
        Input(
            component_id="payload-slider",
            component_property="value"
        )
    ]
)

def get_scatter_chart(entered_site, payload_range):

    # Extract selected payload limits
    low, high = payload_range

    # Filter dataset based on payload range
    filtered_df = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= low) &
        (spacex_df["Payload Mass (kg)"] <= high)
    ]

    # Filter based on selected launch site
    if entered_site != "ALL":

        filtered_df = filtered_df[
            filtered_df["Launch Site"] == entered_site
        ]

    # Create scatter plot
    fig = px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        title="Payload Mass vs. Launch Outcome",
        labels={
            "class": "Launch Outcome",
            "Payload Mass (kg)": "Payload Mass (Kg)",
            "Booster Version Category": "Booster Version"
        },
        hover_data=["Launch Site"]
    )

    return fig


# --------------------------------------------------
# 5. Run application
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True, port=8050)