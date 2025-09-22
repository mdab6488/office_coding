# Pattern 1: Handling form validation
def user_registration(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters")
            
        user = User.objects.create_user(username, email, password)
        
    except KeyError as e:
        return JsonResponse({
            'status': 'error',
            'message': f'Missing field: {e}'
        }, status=400)
        
    except ValidationError as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)
        
    except IntegrityError as e:
        return JsonResponse({
            'status': 'error',
            'message': 'Username or email already exists'
        }, status=409)
        
    else:
        # Send welcome email only if registration was successful
        send_welcome_email(user)
        return JsonResponse({
            'status': 'success',
            'message': 'User registered successfully'
        })

# Pattern 2: API response handling with external services
def fetch_weather_data(city):
    try:
        response = requests.get(
            f"https://api.weather.com/v1/cities/{city}/forecast",
            timeout=5  # Set timeout to avoid hanging
        )
        response.raise_for_status()  # Raises HTTPError for bad status codes
        return response.json()
        
    except requests.exceptions.Timeout:
        logger.error("Weather API timeout for city: %s", city)
        return None  # Could implement retry logic here
        
    except requests.exceptions.HTTPError as e:
        logger.error("Weather API HTTP error: %s", e)
        if response.status_code == 404:
            raise ValueError(f"Weather data not available for {city}")
        else:
            raise Exception("Weather service temporarily unavailable")
            
    except requests.exceptions.RequestException as e:
        logger.error("Weather API request failed: %s", e)
        raise Exception("Failed to connect to weather service")