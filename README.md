## Skincare Recommender Tool
# Overview
Online skincare shopping can be overwhelming—especially when you're faced with dozens of similar products and limited filters like price or rating. This tool aims to simplify the process by offering a smarter way to compare skincare products, taking into account your skin type and other priorities like product category, price, and rating.

Unlike typical e-commerce sites, this recommender leverages over 600,000 reviews from real users and filters them based on skin type (dry, oily, combination, or normal). Whether you're looking for the best sunscreen for oily skin or a moisturizer that works well for combination types, this tool can help you make more informed, personalized decisions—without opening 10 tabs.

# Features
Personalized product filtering by:
- Skin type
- Product type (e.g., sunscreen, moisturizer)
- Price range
Overall rating
- Aggregated reviews from shoppers with similar skin concerns
- Simplified shopping experience by enabling comparison of multiple products in one place

# Data Source
The data comes from Kaggle:
Sentiment Analysis: Sephora Reviews
It includes:
- 8,000+ product listings
- 600,000+ user reviews
  - Product details: brand, price, ingredients, size, and more
  - User details: skin type, age range, product recommendation

# Setup Instructions

1. Clone Repository
  git clone (https://github.com/Cefrida/skincare.git )
  cd skincare-recommender
2. Create a virtual environemnt (not required but recommended)
   python -m venv venv
  source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dash
  pip install dash
4. Navigate and run
   Navigate to where you have stored the file using "cd"
   Run the dash using "python3 app.py"

   


