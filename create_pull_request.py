import requests
import json

# Constants
GITHUB_API_URL = "https://api.github.com"
REPO_OWNER = "Vanshikapandey30"  # Original repository owner
REPO_NAME = "HacktoberFest2024"   # Original repository name
YOUR_USERNAME = "your_github_username"  # Your GitHub username
YOUR_REPO = f"{YOUR_USERNAME}/{REPO_NAME}"

# Function to create a pull request
def create_pull_request(branch_name, title, body):
    url = f"{GITHUB_API_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    headers = {
        "Authorization": f"token YOUR_GITHUB_TOKEN",  # Replace with your GitHub personal access token
        "Accept": "application/vnd.github.v3+json",
    }
    
    # Pull request data
    data = {
        "title": title,
        "head": YOUR_USERNAME + ":" + branch_name,  # Your branch in your fork
        "base": "main",  # The branch you want to merge into (typically 'main' or 'master')
        "body": body
    }
    
    # Create pull request
    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    if response.status_code == 201:
        print("Pull request created successfully!")
        print("Pull Request URL:", response.json()['html_url'])
    else:
        print("Failed to create pull request")
        print("Response:", response.json())

if __name__ == "__main__":
    # Get user input for pull request details
    branch_name = input("Enter your branch name: ")
    title = input("Enter the title of your pull request: ")
    body = input("Enter a description for your pull request: ")
    
    create_pull_request(branch_name, title, body)
