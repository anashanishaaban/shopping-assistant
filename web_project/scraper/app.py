from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="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"
)

# Define the default route to return the index.html file
@app.route("/")
def index():
    return render_template("Landing.html")

@app.route('/login')
def login():
    return render_template('Login.html')

# Define the /api route to handle POST requests
@app.route("/api", methods=["POST"])
def api():
    # Get the message from the POST request
    message = request.json.get("message")
    # Send the message to OpenAI's API and receive the response
    
    
    chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user", 
            "content": message
        }
    ]
    )

    if chat_completion.choices[0].message.content!=None:
        return chat_completion.choices[0].message.content

    else :
        return 'Failed to Generate response!'

if __name__=='__main__':
    app.run()
