from flask import Flask, jsonify, request
import database

app = Flask(__name__)
database.init_db()

@app.route('/api/users', methods=['GET'])
def get_users():
    with database.get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, username, email FROM users')
        users = [dict(id=row[0], username=row[1], email=row[2]) for row in cursor.fetchall()]
    return jsonify(users)

@app.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    if not user_data or 'username' not in user_data or 'email' not in user_data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    with database.get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO users (username, email) VALUES (?, ?)',
                (user_data['username'], user_data['email'])
            )
            conn.commit()
            return jsonify({'id': cursor.lastrowid, **user_data}), 201
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Username or email already exists'}), 400

if __name__ == '__main__':
    app.run(debug=True)
