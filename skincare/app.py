
# Import necessary libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Create a Dash application
app = dash.Dash(__name__)

# Load your data (e.g., merged_df)
merged_df = pd.read_csv('/data/filtered_reviews.csv')
 # Replace with the path to your data

# Define the layout of the app
app.layout = html.Div([
    dcc.Dropdown(id='secondary-category-dropdown', 
                 options=[{'label': 'Category 1', 'value': 'cat1'}, {'label': 'Category 2', 'value': 'cat2'}],
                 value='cat1'),
    dcc.Dropdown(id='skin-type-dropdown', 
                 options=[{'label': 'Dry', 'value': 'dry'}, {'label': 'Oily', 'value': 'oily'}],
                 value='dry'),
    dcc.Dropdown(id='user-preference-dropdown', 
                 options=[{'label': 'Low Price', 'value': 'low_price'}, {'label': 'Best Rated', 'value': 'best_rated'}],
                 value='low_price'),
    html.Div(id='recommendation-table')  # Where the table will be displayed
])

# Define callback to update table based on inputs
@app.callback(
    Output('recommendation-table', 'children'),
    Input('secondary-category-dropdown', 'value'),
    Input('skin-type-dropdown', 'value'),
    Input('user-preference-dropdown', 'value')
)
def update_recommendations(secondary_category, skin_type, user_preference):
    filtered_df = merged_df[(merged_df["secondary_category"] == secondary_category) & 
                            (merged_df["is_recommended"] == 1) & 
                            (merged_df["skin_type"] == skin_type)]

    skin_type_ratings = filtered_df.groupby('product_name').agg({
        'indv_rating': 'mean',
        'price_usd': 'mean'
    }).reset_index()

    sorted_df = skin_type_ratings.sort_values(
        "price_usd" if user_preference == "low_price" else "indv_rating", 
        ascending=(user_preference == "low_price")
    )

    top_products = sorted_df.head(10)

    # Turn into Dash HTML Table
    return [
        html.Table([
            html.Thead(html.Tr([html.Th(col) for col in top_products.columns])),
            html.Tbody([
                html.Tr([html.Td(row[col]) for col in top_products.columns]) 
                for _, row in top_products.iterrows()
            ])
        ])
    ]

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
