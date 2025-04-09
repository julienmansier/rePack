import argparse
import os
import json

def validate_file(file_path):
    """Validate that the given file exists and is readable."""
    if not os.path.isfile(file_path):
        raise argparse.ArgumentTypeError(f"File '{file_path}' does not exist.")
    if not os.access(file_path, os.R_OK):
        raise argparse.ArgumentTypeError(f"File '{file_path}' is not readable.")
    return file_path

def validate_directory(directory_path):
    """Validate that the given directory exists and is writable."""
    if not os.path.isdir(directory_path):
        raise argparse.ArgumentTypeError(f"Directory '{directory_path}' does not exist.")
    if not os.access(directory_path, os.W_OK):
        raise argparse.ArgumentTypeError(f"Directory '{directory_path}' is not writable.")
    return directory_path

def main():
    parser = argparse.ArgumentParser(description="Process a JSON file and a directory.")
    parser.add_argument("json_file", type=validate_file, help="Path to the JSON file")
    parser.add_argument("directory", type=validate_directory, help="Path to the directory")
    
    args = parser.parse_args()
    
    # Load and print the JSON file content
    with open(args.json_file, 'r') as json_file:
        data = json.load(json_file)
        
    
    #print(f"Directory '{args.directory}' is valid.")

if __name__ == "__main__":
    main()
