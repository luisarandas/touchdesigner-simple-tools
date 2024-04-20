# luis arandas 20-04-2024
import requests
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[
                        logging.FileHandler("debug.log"),
                        logging.StreamHandler()
                    ])

def send_test_data():
    url = 'http://127.0.0.1:9980'
    data = {'test_key': 'test_value'}
    headers = {'Content-Type': 'application/json'}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Will raise an exception for HTTP errors
        logging.info("Server response: %s", response.text)
    except requests.exceptions.HTTPError as http_err:
        logging.error("HTTP error occurred: %s - %s", http_err, response.status_code)
        logging.error("Response body: %s", response.text)
    except requests.exceptions.ConnectionError:
        logging.error("Connection error: Could not connect to server.")
    except requests.exceptions.Timeout:
        logging.error("Timeout error: The request timed out.")
    except requests.exceptions.RequestException as err:
        logging.error("An error occurred: %s", err)

send_test_data()
