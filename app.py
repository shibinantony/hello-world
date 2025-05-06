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
            img, iframe { /* Added iframe styling */
                margin: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
                max-width: 100%; /* Ensure content is responsive */
                height: auto; /* Adjusted for iframe aspect ratio */
            }
            iframe { /* Specific iframe height adjustment */
                /* Original width: 560, Original height: 315 (16:9 aspect ratio) */
                /* New width (560 * 1.4) = 784 */
                /* New height (315 * 1.4) = 441 */
                 width: 784px; /* Updated width */
                 height: 441px; /* Updated height */
                 max-width: 100%;
                 aspect-ratio: 16 / 9; /* Maintain video aspect ratio */
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Test page by Shibin Antony Boban.</h1>
            <p>Proof of Concept for Webapp deployment on Azure</p>

            <iframe width="784" height="441" src="https://www.youtube-nocookie.com/embed/AyzJyWGqm0c?si=oEckVtcRg3zhFTwT&amp;start=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

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
if __name__ == '__main__':
    # Run the Flask development server.
    # For production on Azure, you would typically rely on the WSGI server (Gunicorn)
    # to bind to the correct port specified by Azure.
    app.run(host='0.0.0.0', port=8080)
