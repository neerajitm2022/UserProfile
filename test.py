print("TEst")
print("This code only exist in local branch")
print("This is new change")
import requests
def call_api():
    url = 'http://127.0.0.1:8000/allpages'
    #headers = {'Accept': 'application/json'}  # Specify the accepted content type
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        # Assuming the response is JSON data
        data = response.json()
        # Process the data here
        print(data)
    except requests.exceptions.RequestException as e:
        # Handle errors
        print("Error:", e)
call_api()
