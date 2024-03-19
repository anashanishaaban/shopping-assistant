import requests
import pandas as pd
'''
# Set up the request parameters
params = {
    'api_key': '7E9E4E160584452791B7CB9E8829AACD',
    'type': 'search',
    'amazon_domain': 'amazon.com',
    'search_term': 'gaming mouse',
    'output': 'csv'
}

# Make the HTTP GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)

# Save the CSV response to a file
with open('output.csv', 'wb') as file:
    file.write(api_result.content)
    
'''

# Load the CSV file into a DataFrame
data = pd.read_csv('output.csv')

# Selecting the required columns
selected_data = data[[
    'search_results.title', 
    'search_results.asin', 
    'search_results.link', 
    'search_results.image', 
    'search_results.rating', 
    'search_results.ratings_total', 
    'search_results.sponsored', 
    'search_results.price.value'
]]

# Check the first few rows of the selected columns to ensure correctness
print(selected_data.head())