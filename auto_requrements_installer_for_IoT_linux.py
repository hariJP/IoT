import subprocess

# Check if pip3 is installed
try:
    subprocess.check_output(["which", "pip3"])
    print("pip3 is already installed.")
except subprocess.CalledProcessError:
    print("pip3 is not installed. Installing pip3...")
    subprocess.call(["sudo", "apt-get", "update"])
    subprocess.call(["sudo", "apt-get", "install", "python3-pip"])

# Install required packages
print("Installing required packages...")
subprocess.call(["pip3", "install", "matplotlib", "oauth2client", "gspread", "pandas"])
print("All required packages installed successfully.")
