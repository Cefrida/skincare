import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Create the Dash app
app = dash.Dash(__name__)

# Load your dataset
merged_df = pd.read_csv('data/skincare_final_data.csv')

# Get unique categories and skin types
categories = merged_df['secondary_category'].unique()
skin_types = merged_df['skin_type'].unique()

# App layout
app.layout = html.Div([
    html.Label('Category:'),
    dcc.Dropdown(
        id='secondary-category-dropdown',
        options=[{'label': category, 'value': category} for category in categories],
        value=categories[0]
    ),

    html.Label('Skin Type:'),
    dcc.Dropdown(
        id='skin-type-dropdown',
        options=[{'label': skin_type, 'value': skin_type} for skin_type in skin_types],
        value=skin_types[0]
    ),

    html.Label('Preference:'),
    dcc.Dropdown(
        id='user-preference-dropdown',
        options=[
            {'label': 'Best Rated', 'value': 'best_rated'},
            {'label': 'Low Price', 'value': 'low_price'}
        ],
        value='low_price'
    ),

    html.Br(),
    html.Div(id='recommendation-table'),

    html.Br(),
    html.Label("Pick Two Products to Compare:"),
    dcc.Dropdown(id='product-comparison-dropdown', multi=True),
    html.Div(id='comparison-result')
])

# Callback to update recommendation table and product comparison dropdown
@app.callback(
    Output('recommendation-table', 'children'),
    Output('product-comparison-dropdown', 'options'),
    Input('secondary-category-dropdown', 'value'),
    Input('skin-type-dropdown', 'value'),
    Input('user-preference-dropdown', 'value')
)
def show_recommendations(secondary_category, skin_type, user_preference):
    filtered_df = merged_df[(merged_df["secondary_category"] == secondary_category) & (merged_df["is_recommended"] == 1)]
    filtered_df_skin_type = filtered_df[filtered_df["skin_type"] == skin_type]

    skin_type_ratings = filtered_df_skin_type.groupby('product_name').agg({
        'indv_rating': 'mean',
        'price_usd': 'mean'
    }).reset_index()

    product_ratings = filtered_df.groupby('product_name').agg({
        'avg_rating': 'first',
        'price_usd': 'mean'
    }).reset_index()

    product_ratings = pd.merge(product_ratings, skin_type_ratings, on='product_name', suffixes=('_overall', '_skin_type'))

    if user_preference == "low_price":
        sorted_df = product_ratings.sort_values("price_usd_overall", ascending=True)
    elif user_preference == "best_rated":
        sorted_df = product_ratings.sort_values("indv_rating", ascending=False)

    top_recommendations = sorted_df[['product_name', 'indv_rating', 'price_usd_skin_type']].head(10)
    top_recommendations = top_recommendations.rename(columns={
        'product_name': 'Product Name',
        'indv_rating': 'Rating',
        'price_usd_skin_type': 'Price (USD)'
    })

    table = html.Table([
        html.Thead(html.Tr([html.Th(col) for col in top_recommendations.columns])),
        html.Tbody([
            html.Tr([
                html.Td(row['Product Name']),
                html.Td(round(row['Rating'], 2)),
                html.Td(f"${row['Price (USD)']:.2f}")
            ])
            for _, row in top_recommendations.iterrows()
        ])
    ])

    options = [{'label': name, 'value': name} for name in top_recommendations['Product Name']]
    return table, options

# Callback to handle product comparison
@app.callback(
    Output('comparison-result', 'children'),
    Input('product-comparison-dropdown', 'value')
)
def compare_products(selected_products):
    if not selected_products or len(selected_products) != 2:
        return html.Div("Please select exactly two products to compare.")

    df_compare = merged_df[merged_df['product_name'].isin(selected_products)]

    score_df = df_compare.groupby('product_name')['avg_combined_score_per_product'].mean().reset_index()
    price_df = df_compare.groupby('product_name')['price_usd'].mean().reset_index()

    compare_df = pd.merge(score_df, price_df, on='product_name')
    compare_df = compare_df.rename(columns={
        'product_name': 'Product Name',
        'avg_combined_score_per_product': 'Combined Score',
        'price_usd': 'Price (USD)'
    })

    compare_df = compare_df.sort_values(by='Combined Score', ascending=False)
    winner = compare_df.iloc[0]

    return html.Div([
        html.H5(" Comparison Result:"),
        html.Table([
            html.Tr([html.Th("Product Name"), html.Th("Combined Score"), html.Th("Price")]),
            *[
                html.Tr([
                    html.Td(row['Product Name']),
                    html.Td(round(row['Combined Score'], 2)),
                    html.Td(f"${row['Price (USD)']:.2f}")
                ]) for _, row in compare_df.iterrows()
            ]
        ]),
        html.Br(),
        html.Div(f"🏆 Based on combined score, **{winner['Product Name']}** is the better choice!", style={'fontWeight': 'bold', 'color': 'green'})
    ])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
