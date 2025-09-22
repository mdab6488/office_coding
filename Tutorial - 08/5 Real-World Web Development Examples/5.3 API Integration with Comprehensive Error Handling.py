# Example 1: Robust API client with retry logic
class APIClient:
    def __init__(self, base_url, timeout=10, max_retries=3):
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = requests.Session()
        
    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        
        for attempt in range(self.max_retries):
            try:
                response = self.session.request(
                    method, url, 
                    timeout=self.timeout,
                    **kwargs
                )
                response.raise_for_status()
                return response.json()
                
            except requests.exceptions.Timeout:
                if attempt == self.max_retries - 1:
                    logger.error("API request timed out after %d attempts", self.max_retries)
                    raise ServiceTimeoutError(f"Request to {url} timed out")
                logger.warning("API request timeout, attempt %d/%d", attempt + 1, self.max_retries)
                time.sleep(2 ** attempt)  # Exponential backoff
                
            except requests.exceptions.HTTPError as e:
                status_code = e.response.status_code
                if 400 <= status_code < 500:
                    # Client error, don't retry
                    if status_code == 404:
                        raise ResourceNotFoundError(f"Resource not found: {url}") from e
                    elif status_code == 429:
                        raise RateLimitError("API rate limit exceeded") from e
                    else:
                        raise ClientError(f"Client error: {status_code}") from e
                else:
                    # Server error, retry
                    if attempt == self.max_retries - 1:
                        raise ServerError(f"Server error: {status_code}") from e
                    logger.warning("Server error %s, attempt %d/%d", status_code, attempt + 1, self.max_retries)
                    time.sleep(2 ** attempt)
                    
            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    raise ConnectionError(f"Failed to connect to {url}") from e
                logger.warning("Connection error, attempt %d/%d", attempt + 1, self.max_retries)
                time.sleep(2 ** attempt)
        
        raise ConnectionError(f"Failed after {self.max_retries} attempts")

# Example 2: Using the API client
def fetch_weather_data(city):
    client = APIClient("https://api.weather.com", max_retries=3)
    try:
        return client.request("GET", f"v1/forecast/{city}")
    except ResourceNotFoundError:
        logger.warning("Weather data not found for city: %s", city)
        return None
    except (ServiceTimeoutError, ServerError, ConnectionError) as e:
        logger.error("Weather service unavailable: %s", e)
        raise ServiceUnavailableError("Weather service temporarily unavailable") from e