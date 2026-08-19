from app import app
# Import the Flask application instance (`app`) from the `app` package.

if __name__ == "__main__":
    # Check if this script is being run directly (not imported).
    app.run(debug=True)
    # Start the Flask development server.
    # `debug=True` enables debug mode for development, providing error logs and auto-restart on code changes.

