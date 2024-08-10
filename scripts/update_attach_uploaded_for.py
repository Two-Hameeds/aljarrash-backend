import requests

API_URL = "https://your-api-url.com/projects/"

def get_project_ids():
    response = requests.get(API_URL, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        projects = response.json()
        # Iterate over the projects and print their id and global_id
        for project in projects:
            print(f"Project ID: {project['id']}, Global ID: {project['global_id']}")
    else:
        print(f"Failed to retrieve projects. Status code: {response.status_code}")

if __name__ == "__main__":
    get_project_ids()