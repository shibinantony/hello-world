# Import the Flask class from the flask library
from flask import Flask

# Create an instance of the Flask application.
# The __name__ argument tells Flask where to look for static files and templates.
app = Flask(__name__)

# Define a route for the root URL ('/').
# When a user visits the root URL of your web application,
# the function decorated by @app.route('/') will be executed.
@app.route('/')
def index():
    """
    This function is the handler for the root URL.
    It now returns HTML content including random images and a message.
    """
    # HTML content to display
    # We'll use Placehold.co to get random placeholder images.
    # You can change the dimensions (e.g., 400x300) or add text to the images.
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Under Development</title>
        <style>
            body {
                font-family: sans-serif;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                min-height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
                color: #333;
            }
            .container {
                text-align: center;
                background-color: #fff;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #555;
                margin-bottom: 20px;
            }
            img {
                margin: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                max-width: 100%; /* Ensure images are responsive */
                height: auto;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Shibin is working on it.</h1>
            <p>Check back later for updates!</p>
            <img src="https://centralofsuccess.com/wp-content/uploads/2017/11/There-is-simply-no-substitute-for-hard-work-when-it-comes-to-achieving-success..png" alt="Placeholder Image 1">
            <img src="https://theinspiringjournal.com/wp-content/uploads/2023/04/keep-working-hard-quotes.jpg" alt="Placeholder Image 2">
            <img src="https://placehold.co/400x250/3357FF/white?text=Image+3" alt="Placeholder Image 3">
        </div>
    </body>
    </html>
    """
    return html_content

# This block allows you to run the Flask application directly from the Python script
# using `python app.py`.
# When deploying to production environments like Azure App Services,
# a production-ready WSGI server (like Gunicorn) will typically run your app,
# and this block will not be executed.
if __name__ == '__main__':
    # Run the Flask development server.
    # host='0.0.0.0' makes the server accessible externally (useful in some deployment scenarios,
    # though Azure handles this differently).
    # port=8080 is a common port for web applications, but on Azure,
    # the port is usually specified by the environment variable PORT.
    # For local testing, 8080 is fine.
    # For production on Azure, you would typically rely on the WSGI server (Gunicorn)
    # to bind to the correct port specified by Azure.
    app.run(host='0.0.0.0', port=8080)
