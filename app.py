from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define dark color styling
    background_color = "#333"
    text_color = "#fff"

    # Pass styling variables to the template
    return render_template('index.html', background_color=background_color, text_color=text_color)

if __name__ == '__main__':
    app.run(debug=False)
