import subprocess

def run_linter():
    result = subprocess.run(["pylint", "app.py"], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    print(run_linter())