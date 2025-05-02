from flask import Flask

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def index():
    """
    This function is called when the root URL is accessed.
    It returns the "Under construction." message.
    """
    return "Under construction."

# This block allows running the app directly using 'python app.py'
# In production on Azure, gunicorn or a similar WSGI server will run the app.
if __name__ == '__main__':
    # Listen on all public IPs (0.0.0.0) and port 8080
    # Azure App Services expects the application to listen on a specific port,
    # often provided via an environment variable (like PORT).
    # For local testing, 8080 is common.
    # For Azure, you'll likely need to adapt this or let the server handle it.
    # A common practice is to use the PORT environment variable:
    # import os
    # port = int(os.environ.get('PORT', 8080))
    # app.run(host='0.0.0.0', port=port)
    
    # For this simple example, we'll keep it basic for local running:
    app.run(host='0.0.0.0', port=8080)
