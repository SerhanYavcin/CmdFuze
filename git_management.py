import subprocess

def git_pull(directory):
    try:
        subprocess.run(["git", "pull"], cwd=directory, check=True)
        print(f"Successfully pulled changes from {directory}.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while pulling: {e}")

def git_push(directory, message):
    try:
        subprocess.run(["git", "add", "."], cwd=directory, check=True)
        subprocess.run(["git", "commit", "-m", message], cwd=directory, check=True)
        subprocess.run(["git", "push"], cwd=directory, check=True)
        print(f"Successfully pushed changes to {directory}.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while pushing: {e}")
