from flask import Blueprint, jsonify, abort

main = Blueprint('main', __name__)

@main.route('/')
def home():
    """
    Route to handle the home page requests, returning a simple JSON greeting.
    """
    return jsonify({"message": "Hello, World!"})

@main.route('/api/data', methods=['GET'])
def get_data():
    """
    Route to provide example data in JSON format. Simulates data retrieval.
    """
    try:
        data = {"message": "Data successfully retrieved!", "data": [1, 2, 3, 4, 5]}
        return jsonify(data)
    except Exception as e:
        print(f"Error retrieving data: {e}", file=sys.stderr)
        abort(500, description="Internal Server Error")

@main.app_errorhandler(404)
def not_found_error(error):
    """Custom error handler for 404 Not Found errors."""
    return jsonify({'error': 'Resource not found'}), 404

@main.app_errorhandler(500)
def internal_error(error):
    """Custom error handler for 500 Internal Server Error."""
    return jsonify({'error': 'Internal server error'}), 500