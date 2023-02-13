from flask import Flask, request, render_template
import openai

# Initialize the Flask app
app = Flask(__name__)

# Configure the OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    # Retrieve the input text from the form
    input_text = request.form.get("input_text")

    # Generate a response using OpenAI's GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text

    # Render the response
    return render_template("index.html", response=response, input_text=input_text)

if __name__ == "__main__":
    app.run(debug=True)
