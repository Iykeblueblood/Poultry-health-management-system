import os
from pathlib import Path

# Get the directory where this script is located (your project's root)
project_root = Path(__file__).parent

# Define the path for the .streamlit folder
streamlit_folder_path = project_root / ".streamlit"

# Define the path for the secrets.toml file
secrets_file_path = streamlit_folder_path / "secrets.toml"

# Content to write into the secrets file
secrets_content = """# This file stores your secret API keys.
# Do NOT commit this file to GitHub!

GEMINI_API_KEY = "PASTE_YOUR_API_KEY_HERE"
"""

try:
    # --- Step 1: Create the .streamlit directory ---
    print(f"Checking for directory: {streamlit_folder_path}")
    os.makedirs(streamlit_folder_path, exist_ok=True)
    print("✅ '.streamlit' directory is present.")

    # --- Step 2: Create and write to the secrets.toml file ---
    if not secrets_file_path.exists():
        print(f"Creating secrets file at: {secrets_file_path}")
        secrets_file_path.write_text(secrets_content)
        print("✅ 'secrets.toml' file created successfully.")
        print("\nIMPORTANT: Now open the '.streamlit/secrets.toml' file and replace 'PASTE_YOUR_API_KEY_HERE' with your actual API key.")
    else:
        print("✅ 'secrets.toml' file already exists. No changes made.")
        print("\nPlease ensure your API key is correctly entered in the file.")

except Exception as e:
    print(f"❌ An error occurred: {e}")