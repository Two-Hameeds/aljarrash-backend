import requests

API_URL = "https://jellyfish-app-ebfd5.ondigitalocean.app/api/design/"

def get_project_ids():
    response = requests.get(API_URL)

    if response.status_code == 200:
        projects = response.json()
        for project in projects:
            print(f"Project ID: {project['id']}, Global ID: {project['global_id']}")
    else:
        print(f"Failed to retrieve projects. Status code: {response.status_code}")

if __name__ == "__main__":
    get_project_ids()