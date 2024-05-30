# In app/routes.py
from flask import Blueprint, jsonify, abort

# Define the Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def home():
    """
    Route to handle the home page requests. Returns a simple JSON greeting.
    """
    return jsonify({"message": "Hello, World!"}), 200

@main.route('/api/data', methods=['GET'])
def get_data():
    """
    Route to provide example data in JSON format. This is a placeholder for
    where you would integrate actual data fetching logic, potentially from
    a database or external service.
    """
    try:
        # Simulated data retrieval logic
        data = {
            "message": "Data successfully retrieved!",
            "data": [1, 2, 3, 4, 5]
        }
        return jsonify(data), 200
    except Exception as e:
        # In a real application, log the exception to a file or logging service
        print(f"Error retrieving data: {str(e)}")  # Placeholder for actual logging
        abort(500, description="Internal Server Error")

@main.app_errorhandler(404)
def not_found_error(error):
    """
    Custom error handler for 404 Not Found errors.
    """
    return jsonify({'error': 'Resource not found'}), 404

@main.app_errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 Internal Server Error.
    """
    return jsonify({'error': 'Internal server error'}), 500
