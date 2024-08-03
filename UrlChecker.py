import argparse
import requests
import random
from pathlib import Path
from colorama import init, Fore
from requests.exceptions import RequestException
from urllib.parse import urlparse

# Initialize Colorama
init(autoreset=True)

# List of User Agents for --random-agent option
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0"
]

def fetch_url(url, random_agent=False):
    headers = {}
    if random_agent:
        headers['User-Agent'] = random.choice(USER_AGENTS)

    try:
        response = requests.get(url, headers=headers)
        return response.status_code, response.reason
    except RequestException as e:
        return None, str(e)

def color_status_code(status_code):
    if status_code == 200:
        return Fore.GREEN
    elif status_code == 301:
        return Fore.BLUE
    elif status_code == 404:
        return Fore.YELLOW
    elif status_code == 403:
        return Fore.RED
    else:
        return Fore.WHITE

def main():
    parser = argparse.ArgumentParser(description="Check status of URLs")
    parser.add_argument('-u', '--url', type=str, help='Single URL to check')
    parser.add_argument('-l', '--list', type=str, help='File containing list of URLs to check')
    parser.add_argument('--random-agent', action='store_true', help='Use a random user agent for each request')
    parser.add_argument('--output', type=str, required=True, help='Output file name (without extension)')
    args = parser.parse_args()

    urls = []
    if args.url:
        urls.append(args.url)
    elif args.list:
        try:
            with open(args.list, 'r') as file:
                urls = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            print(f"File {args.list} not found.")
            return

    output_file_path = Path(args.output).with_suffix('.txt')
    
    with output_file_path.open('w') as output_file:
        for url in urls:
            # Parse URL to ensure it's correctly handled
            parsed_url = urlparse(url)
            if not parsed_url.scheme:
                url = 'http://' + url
            
            status_code, reason = fetch_url(url, args.random_agent)
            if status_code is None:
                output = f"{url} [Error: {reason}]"
                print(Fore.RED + output)
                output_file.write(output + "\n")
            else:
                color = color_status_code(status_code)
                output = f"{url} [{status_code} {reason}]"
                print(color + output)
                output_file.write(output + "\n")

if __name__ == "__main__":
    main()
