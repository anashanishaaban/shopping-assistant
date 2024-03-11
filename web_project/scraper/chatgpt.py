from openai import OpenAI
OPENAI_API_KEY="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"
client = OpenAI(api_key=OPENAI_API_KEY)

data = "import from csv file"

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a data sorter for an e-commerce website"},
    {"role": "user", "content": f"only display this data:{data}"}
  ]
)

print(completion.choices[0].message)
