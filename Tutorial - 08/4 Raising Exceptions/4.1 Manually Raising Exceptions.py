# You can raise exceptions intentionally using the raise statement, which is useful for validating inputs or signaling error conditions in your web application.

# Example 1: Raising exceptions for validation
def validate_user_input(user_data):
    if not user_data.get('username'):
        raise ValueError("Username is required")
    
    if len(user_data.get('password', '')) < 8:
        raise ValueError("Password must be at least 8 characters")
    
    if not re.match(r'[^@]+@[^@]+\.[^@]+', user_data.get('email', '')):
        raise ValueError("Invalid email format")
    
    return True

# Example 2: Raising exceptions with custom messages
def process_payment(amount, card_info):
    if amount <= 0:
        raise ValueError(f"Invalid payment amount: {amount}")
    
    if not is_valid_card(card_info):
        raise ValueError("Invalid card information")
    
    try:
        result = payment_gateway.charge(amount, card_info)
    except payment_gateway.GatewayError as e:
        # Log the original error and raise a new exception
        logger.error("Payment gateway error: %s", e)
        raise Exception("Payment processing temporarily unavailable") from e
    
    return result

# Example 3: Using raise without specifying an exception (re-raising)
try:
    dangerous_operation()
except Exception as e:
    logger.error("Operation failed: %s", e)
    # Re-raise the same exception after logging
    raise