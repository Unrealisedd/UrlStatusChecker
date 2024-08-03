# URL Status Checker

This Python script checks the HTTP status of given URLs and outputs the results both to the console and a text file. The script can handle a single URL or a list of URLs, and it includes options for using random user agents and customizing the output file name.

## Features

- Check the HTTP status of a single URL or a list of URLs.
- Use a random User-Agent for each request to avoid detection.
- Output the status of each URL in the console with color coding for easy identification.
- Save the results to a specified output file.

## Requirements

- Python 3.12 or higher
- `requests` library
- `colorama` library


## Usage
Command Line Options
-u, --url: Specify a single URL to check.
-l, --list: Specify a file containing a list of URLs to check.
--random-agent: Use a random User-Agent for each request.
--output: Specify the name of the output file (default is output.txt).

## Examples
Check a Single URL
python script.py -u https://example.com/id=1

Check a Single URL with multiple Parameters
python script.py -u "https://example.com/id=1&lan=en"

Check Multiple URLs from a File
python script.py -l urls.txt

Use a Random User-Agent
python script.py -u https://www.example.com --random-agent

Specify an Output File
python script.py -u https://www.example.com --output results.txt



## Output
The script prints the status of each URL to the console with the following color coding:

Green for 200 OK

Blue for 301 Redirect

Yellow for 404 Not Found

Red for 403 Forbidden

White for other status codes

The script also saves the results to the specified output file.
