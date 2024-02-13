import os
from prettytable import PrettyTable

def calculate_md5(file_path):
    """Calculate MD5 hash of a file."""
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def generate_md5_table(directory):
    """Generate a pretty table of MD5 hashes for files in a directory."""
    table = PrettyTable(["File", "MD5 Hash"])
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            md5_hash = calculate_md5(file_path)
            table.add_row([file_name, md5_hash])
    return table

if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    if os.path.isdir(directory):
        md5_table = generate_md5_table(directory)
        print(md5_table)
    else:
        print("Invalid directory path.")