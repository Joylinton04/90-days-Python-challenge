# Day 14 of py challenge
# Write a program that interacts with the GitHub API to fetch user data (like profile information).

import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses (like 404)

        user_data = response.json()
        print(f"\nGitHub User: {username}")
        print("-" * 40)
        print(f"Name: {user_data.get('name', 'N/A')}")
        print(f"Bio: {user_data.get('bio', 'N/A')}")
        print(f"Location: {user_data.get('location', 'N/A')}")
        print(f"Public Repos: {user_data.get('public_repos', 'N/A')}")
        print(f"Followers: {user_data.get('followers', 'N/A')}")
        print(f"Following: {user_data.get('following', 'N/A')}")
        print(f"Profile URL: {user_data.get('html_url', 'N/A')}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request failed: {req_err}")

# Example: prompt user for GitHub username
if __name__ == "__main__":
    username = input("Enter GitHub username: ")
    get_github_user(username)
