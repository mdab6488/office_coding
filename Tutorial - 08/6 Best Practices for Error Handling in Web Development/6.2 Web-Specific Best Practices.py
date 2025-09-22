"""User-Friendly Error Messages: Convert technical exceptions into user-friendly messages."""
@app.route('/user/<user_id>')
def user_profile(user_id):
    try:
        user = get_user(user_id)
        return render_template('profile.html', user=user)
    except UserNotFoundError:
        flash('User not found')
        return redirect(url_for('user_list'))
    except DatabaseError:
        flash('Service temporarily unavailable. Please try again later.')
        return redirect(url_for('home'))

"""Proper HTTP Status Codes: Return appropriate HTTP status codes for different error conditions."""
# In a Flask application
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
    
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500
    
# In a view function
@app.route('/api/user/<user_id>')
def api_user_profile(user_id):
    try:
        user = get_user(user_id)
        return jsonify(user.to_dict())
    except UserNotFoundError:
        return jsonify({'error': 'User not found'}), 404
    except DatabaseError:
        return jsonify({'error': 'Service unavailable'}), 503
    
"""Structured Error Responses: For APIs, provide structured error responses with consistent formatting."""
# Standard error response format
def error_response(message, code, details=None):
    response = {
        'error': {
            'code': code,
            'message': message,
            'timestamp': datetime.utcnow().isoformat()
        }
    }
    if details is not None:
        response['error']['details'] = details
    return response
    
# Usage in an API view
@app.route('/api/data')
def get_data():
    try:
        data = fetch_data()
        return jsonify(data)
    except ValidationError as e:
        return jsonify(error_response(
            "Invalid request parameters", 
            400,
            {'fields': e.errors}
        )), 400
    except ServiceUnavailableError as e:
        return jsonify(error_response(
            "Service temporarily unavailable",
            503,
            {'retry_after': 60}
        )), 503