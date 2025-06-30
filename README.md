
# WebCheck


# WebCheck

WebCheck is a simple Python tool to fetch, analyze, and report on web pages. It retrieves the source code, headers, cookies, encoding, redirect history, status code, and performs basic phishing detection for a given URL.

## Features

- Fetches and saves the full web page source code
- Displays HTTP headers and encoding
- Lists cookies set by the page
- Shows redirect history and status code
- Attempts basic phishing detection using URL patterns
- Saves a full report to `output.txt`

## Requirements

- Python 3.6+
- `requests` library

## Installation

```bash
pip install -r requirements.txt