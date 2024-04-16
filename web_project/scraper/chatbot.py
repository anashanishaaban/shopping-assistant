from openai import OpenAI
import pandas as pd

'''def openai_call(request):
 
  client = OpenAI(api_key='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')
  if requests.method == 'POST':
      user_query = request.POST.get('user_query')
      
      # Prepare product data text
      product_data = get_product_data_as_text("output.csv")

      # Create the prompt with product data and user query
      prompt = f"{product_data}\n\n{user_query}"

      # Make the OpenAI API call
      response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
              {"role": "system", "content": product_data},
              {"role": "user", "content": prompt}
          ]
      )
      content = response.choices[0].message.content'''

import os
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
  
def openai_call(prompt):
    response = client.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message['content']

print(openai_call("hello"))

def get_product_data_as_text(file_path):
    # Load the CSV file into a DataFrame
    data = pd.read_csv(file_path)

    # Define the text format for each product
    # You can adjust the details you include as per your CSV file's columns
    product_texts = []
    for index, row in data.iterrows():
        product_text = f"""
        Product: {row['search_results.title']}
        Price: {row['search_results.price.value']} {row['search_results.price.currency']}
        Features: {row.get('search_results.feature', 'N/A')}
        Rating: {row['search_results.rating']} stars
        """
        product_texts.append(product_text.strip())

    # Combine all product texts into a single string
    all_product_text = "\n\n".join(product_texts)
    
    return all_product_text