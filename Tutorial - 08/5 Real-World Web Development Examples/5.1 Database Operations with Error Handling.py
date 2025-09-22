# Example 1: Safe database operations with context managers
def get_user_profile(user_id):
    try:
        with database_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT username, email, created_at FROM users WHERE id = %s",
                    (user_id,)
                )
                row = cursor.fetchone()
                
                if row is None:
                    raise UserNotFoundError(f"User {user_id} not found")
                    
                return {
                    'username': row[0],
                    'email': row[1],
                    'created_at': row[2]
                }
                
    except DatabaseError as e:
        logger.error("Database error while fetching user %s: %s", user_id, e)
        raise ServiceUnavailableError("Database temporarily unavailable") from e
        
    except OperationalError as e:
        logger.error("Operational error in database: %s", e)
        raise ServiceUnavailableError("Service temporarily unavailable") from e

# Example 2: Transaction management with error handling
def transfer_funds(sender_id, receiver_id, amount):
    try:
        with database_connection() as conn:
            with conn.cursor() as cursor:
                # Check sender balance
                cursor.execute(
                    "SELECT balance FROM accounts WHERE user_id = %s",
                    (sender_id,)
                )
                sender_balance = cursor.fetchone()[0]
                
                if sender_balance < amount:
                    raise InsufficientFundsError(
                        f"User {sender_id} has insufficient funds"
                    )
                
                # Deduct from sender
                cursor.execute(
                    "UPDATE accounts SET balance = balance - %s WHERE user_id = %s",
                    (amount, sender_id)
                )
                
                # Add to receiver
                cursor.execute(
                    "UPDATE accounts SET balance = balance + %s WHERE user_id = %s",
                    (amount, receiver_id)
                )
                
                # Record transaction
                cursor.execute(
                    """INSERT INTO transactions 
                       (sender_id, receiver_id, amount, status) 
                       VALUES (%s, %s, %s, 'completed')""",
                    (sender_id, receiver_id, amount)
                )
                
                conn.commit()
                return True
                
    except DatabaseError as e:
        conn.rollback()
        logger.error("Fund transfer failed: %s", e)
        raise TransferFailedError("Fund transfer failed") from e