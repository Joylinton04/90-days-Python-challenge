# Day 26-27: HTTP Header Analysis
# Write a script that fetches HTTP headers from a target URL and checks for common security
# misconfigurations (e.g., missing Strict-Transport-Security header).

import requests

def scan_https_header(url):
    try:
        response = requests.get(url)
        headers = response.headers

        print("Response Headers: ")
        for key, value in headers.items():
            print(f"{key}: {value}")

        print("\nScan results for missing Strict-Transport-Security\n")

        if headers.get('Strict-Transport-Security'):
            print("[+] Strict-Transport-Security: pass")
        else:
            print("[-] Strict-Transport-Security header not present: fail!")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    target_url = input("Enter your target website: ")
    scan_https_header(target_url)
