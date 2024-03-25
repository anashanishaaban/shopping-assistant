import requests
import pandas as pd

def api_call(search_term):

    # Set up the request parameters
    params = {
        'api_key': '7E9E4E160584452791B7CB9E8829AACD',
        'type': 'search',
        'amazon_domain': 'amazon.com',
        'search_term': search_term,
        'output': 'csv'
    }

    # Make the HTTP GET request to Rainforest API
    api_result = requests.get('https://api.rainforestapi.com/request', params)

    # Save the CSV response to a file
    with open('output.csv', 'wb') as file:
        file.write(api_result.content)

def get_product_data_csv(file_path):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(file_path)

    # Selecting the required columns
    selected_columns = [
        'search_results.title', 
        'search_results.asin', 
        'search_results.link', 
        'search_results.image', 
        'search_results.rating', 
        'search_results.ratings_total', 
        'search_results.is_prime', 
        'search_results.sponsored', 
        'search_results.price.currency', 
        'search_results.price.value'
    ]
    
    # Ensure all columns exist, fill missing with 'N/A'
    for col in selected_columns:
        if col not in data.columns:
            data[col] = 'N/A'
    
    # Select the required columns
    selected_data = data[selected_columns]
    
    # Convert boolean to string for consistency with the original function
    selected_data['search_results.is_prime'] = selected_data['search_results.is_prime'].map({True: 'Prime', False: 'Non-Prime', pd.NA: 'N/A'})
    selected_data['search_results.sponsored'] = selected_data['search_results.sponsored'].map({True: 'Sponsored', False: 'Not Sponsored', pd.NA: 'N/A'})
    
    # Convert the DataFrame to a list of dictionaries for easier processing
    products_list = selected_data.to_dict(orient='records')
    
    # Convert each product into a list format
    products_data = []
    for product in products_list:
        product_data = [
            product['search_results.title'],
            product['search_results.asin'],
            product['search_results.link'],
            product['search_results.image'],
            str(product['search_results.rating']) if product['search_results.rating'] != 'N/A' else product['search_results.rating'],
            str(product['search_results.ratings_total']),
            product['search_results.is_prime'],
            product['search_results.sponsored'],
            product['search_results.price.currency'],
            str(product['search_results.price.value']) if product['search_results.price.value'] != 'N/A' else product['search_results.price.value']
        ]
        products_data.append(product_data)
    
    return products_data