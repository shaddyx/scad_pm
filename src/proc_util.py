import subprocess
def call(cwd, process_with_params):
    subprocess.call(process_with_params, cwd=cwd)
