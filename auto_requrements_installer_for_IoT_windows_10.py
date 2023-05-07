import subprocess

# Check if pip is installed, install it if not
try:
    import pip
except ImportError:
    subprocess.run(["python", "-m", "ensurepip", "--default-pip"])

# Install required packages using pip
subprocess.run(["pip", "install", "matplotlib", "oauth2client", "gspread", "pandas"])
