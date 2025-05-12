# Skincare Recommender Tool
## Overview
The Personalized Skincare Recommender is a user-friendly tool designed to help individuals navigate the overwhelming number of skincare products available today. By allowing users to input key details such as their skin type, budget preferences, and product priorities, the tool generates tailored product recommendations that align with their specific needs. This solution is ideal for skincare beginners, busy professionals, or anyone looking to make more informed choices without spending hours researching. What sets it apart from e-commerce filters or other recommenders is its integratio of natural language processing. This has been used to calculate sentiment scores for each review. These scores are then averaged and applied to each product, giving the user the options that best match their profile. 


## How It Works
The dashboard is divided into two main sections:

### 1. Personalized Product Recommendations
Users begin by selecting:

  - A product category (e.g., moisturizers, sunscreen)
  - Their skin type (dry, oily, combination, or normal)
  - A preference: prioritize either higher ratings or lower prices

Based on these inputs, the system returns the top 10 products that best align with the user's criteria. Ratings are calculated using data from reviewers with the same skin type, providing more relevant and accurate recommendations.

### 2. Review-Based Product Comparison
Users can then select two products from their top 10 to compare. The system uses natural language processing (NLP) to analyze the sentiment of real user reviews. Based on these sentiment scores, the dashboard highlights which product is rated more positively by people with similar skincare needs.

## Key Features
  - Built using over 600,000 real user reviews
  - Custom ratings based on skin-type-specific feedback
  - NLP-powered sentiment analysis for in-depth product comparison
  - Simple user interface 

# Folder Structure
skincare/
- README.md
-  app.py
-  skincare_preprocessing.py

data/
- sample_10mb.csv

writeup/
- writeup.pdf

#### app.py 
  - A python file that contains the code for the dash.

#### Skincare_preprocessing.py
  - A python file that contains preprocessing steps for the raw data. This can be run by the user to get the exact final
    code I have displayed in the data folder. The version in the folder is a subset of the full data.

#### sample_10mb.csv
  - A 10mb file containing a subset of the data. This is just for viewership and is not fully representative of the full
    data.
    
#### writeup.pdf
  - The writeup provides a clear, high-level overview of the skincare recommender project, including its motivation, data
    sources, methodology, and use case. It explains how the tool was built, highlights key decisions, and
    demonstrates how the recommender can be used. 


## Data Source
The data comes from Kaggle:
[Sentiment Analysis: Sephora Reviews](https://www.kaggle.com/code/aashidutt3/sentiment-analysis-sephora-reviews#%F0%9F%AA%A7-About-the-Dataset)
It includes:
- 8,000+ product listings (1 file)
   - Product details: brand, price, ingredients, size, etc.
- 600,000+ user reviews (6 files)
  - Reviewer details: skin type, age range, product recommendation
 

## Setup Instructions

1. Clone Repository

2. Create a virtual environemnt (using venv) 
  
3. Navigate and run
   Navigate to where you have stored the file
   Run the dash using "python3 app.py"

   


