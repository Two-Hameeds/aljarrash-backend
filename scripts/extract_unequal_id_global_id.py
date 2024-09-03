import requests

API_URL = "https://jellyfish-app-ebfd5.ondigitalocean.app/api"


def get_unequal_ids():
    response = requests.get(f"{API_URL}/design", headers={"Authorization": "Token becad41b685ebad806be6cf21670632bf3c07643f4541d597ad75fabb2730cd0"})
    projects_count = 0
    comments_count = 0
    if response.status_code == 200:
        projects = response.json()
        for project in projects:
            if not project["id"] == project["global_id"] and project["comments_count"] > 0:
                comments_response = requests.get(f"{API_URL}/comments/?written_for={project['global_id']}", headers={"Authorization": "Token becad41b685ebad806be6cf21670632bf3c07643f4541d597ad75fabb2730cd0"})
                comments = comments_response.json()
                target_project = requests.get(f"{API_URL}/design/{project['global_id']}", headers={"Authorization": "Token becad41b685ebad806be6cf21670632bf3c07643f4541d597ad75fabb2730cd0"}).json()
                new_written_for = target_project["global_id"]
                comments_count = comments_count + len(comments)
                projects_count = projects_count + 1
                print(f"stage: {project["stage"]}")
                print(f"{project['project_name']}: {project['id']}, {project['global_id']} ({project["comments_count"]})", end=".\n")
                print("comments to be updated:")
                for comment in comments:
                    print(f"{comment["id"]} => from: {comment['written_for']}, to: {new_written_for}", end=".\n")
        print(f"\n\n{projects_count=}")
        print(f"{comments_count=}")
    else:
        print(f"Failed to retrieve projects. Status code: {response.status_code}")
        
        
def update_written_for():
    pass
        

get_unequal_ids()