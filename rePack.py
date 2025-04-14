import requests
import subprocess
import os
import argparse



def main():
    parser = argparse.ArgumentParser(description="Process needed files")
    parser.add_argument('--hash', type=str,required=True, help="File Hash")
    parser.add_argument( '--token', type=str,required=True, help="API Token")
    parser.add_argument( '--url', type=str,required=True, help="Spectra Analyze URL")
    args = parser.parse_args()

    # Change the values of hash_value and token
    hash_value = args.hash
    token = args.token
    url = args.url

    url = f"https://{url}/api/samples/{hash_value}/unpacked/"

    headers = {
        "Authorization": f"Token {token}"
    }

    # Add verify=False in the request if you are using a self-signed SSL certificate
    response = requests.get(url, headers=headers)
    response.raw.decode_content = True

    with open("filename", "wb") as f:
        f.write(response.content)
        f.close()

    current_working_directory = os.getcwd()
    dir = current_working_directory+'/'+ hash_value +'.rl/infected/'

    mkdir = subprocess.run(['mkdir', 'extracted'], capture_output=True, text=True)
    unzip = subprocess.run(['tar', 'xvf' ,'filename'], capture_output=True, text=True)
    mv = subprocess.run(['cp', '-r', dir , current_working_directory+'/extracted/'], capture_output=True, text=True)


if __name__ == "__main__":
    main()