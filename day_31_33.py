# Day 31-33: Cross-Site Scripting (XSS) Basics
#  Create a script that detects potential XSS vulnerabilities in a simple web application by checking for
# unsanitized user input.

import requests
from urllib.parse import urlencode

# Common XSS payloads
payloads = [
    "<script>alert(1)</script>",
    "\"><script>alert(1)</script>",
    "'><img src=x onerror=alert(1)>",
    "<svg onload=alert(1)>",
    "<body onload=alert(1)>"
]

def test_xss(url, param):
    print(f"Testing {url} for XSS via parameter '{param}'\n")

    for payload in payloads:
        # Craft query with payload injected
        query = {param: payload}
        test_url = f"{url}?{urlencode(query)}"

        try:
            response = requests.get(test_url, timeout=5)

            if payload in response.text:
                print(f"🚨 Possible XSS detected with payload: {payload}")
                print(f"URL: {test_url}\n")
            else:
                print(f"✅ Payload escaped or not reflected: {payload}")

        except requests.exceptions.RequestException as e:
            print(f"Error during request: {e}")

# Example usage
if __name__ == "__main__":
    # Example: http://localhost:5000/search?query=
    base_url = input("Enter base URL (e.g. http://localhost:5000/search): ")
    param_name = input("Enter parameter name (e.g. query): ")
    
    test_xss(base_url, param_name)
