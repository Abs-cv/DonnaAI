def install_dependencies(dependencies):
    \"\"\"Installs the required dependencies.\"\"\"
    import subprocess
    for dependency in dependencies:
        subprocess.check_call(["pip", "install", dependency])
