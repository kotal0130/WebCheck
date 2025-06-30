import sys
import re
import requests

# Ensure the script is run with Python 3
if sys.version_info[0] < 3:
    print('\n.......please install python3 to run tool.....\n')
    sys.exit()

print("(⓿_⓿) I can help you get a web page source code (‾◡◝)")
url = input('Paste web page link here: ').strip()

if not url.startswith(('http://', 'https://')):
    print("Please enter a valid URL (must start with http:// or https://).")
    sys.exit()

print('\033[2;43m (⌐■_■) Fetching and displaying source code... \033[0;0m')

output_lines = []

try:
    session = requests.Session()
    response = session.get(url, allow_redirects=True, timeout=10)

    # Web page source code
    print("\n>> Web page source code:\n")
    preview = response.text[:2000] + ("\n... [truncated]" if len(response.text) > 2000 else "")
    print(preview)
    output_lines.append(">> Web page source code:\n")
    output_lines.append(response.text)
    output_lines.append("\n")

    # Web page header
    print("\n>> Web page headers:\n")
    output_lines.append(">> Web page headers:\n")
    for k, v in response.headers.items():
        print(f"{k}: {v}")
        output_lines.append(f"{k}: {v}")
    output_lines.append("\n")

    # Web page encoding
    print(f"\n>> Web page encoding: {response.encoding}")
    output_lines.append(f">> Web page encoding: {response.encoding}\n")

    # Web page cookies
    print("\n>> Web page cookies:")
    output_lines.append(">> Web page cookies:")
    if session.cookies:
        for cookie in session.cookies:
            print(f"{cookie.name}: {cookie.value}")
            output_lines.append(f"{cookie.name}: {cookie.value}")
    else:
        print("No cookies set.")
        output_lines.append("No cookies set.")
    output_lines.append("\n")

    # Web page history (redirects)
    print("\n>> Web page history (redirects):")
    output_lines.append(">> Web page history (redirects):")
    if response.history:
        for resp in response.history:
            print(f"{resp.status_code} => {resp.url}")
            output_lines.append(f"{resp.status_code} => {resp.url}")
        print(f"{response.status_code} => {response.url}")
        output_lines.append(f"{response.status_code} => {response.url}")
    else:
        print("No redirects. Final URL:", response.url)
        output_lines.append(f"No redirects. Final URL: {response.url}")
    output_lines.append("\n")

    # Web page status code
    print(f"\n>> Web page status code: {response.status_code}")
    output_lines.append(f">> Web page status code: {response.status_code}\n")

    # Request recent page logs - Not possible in general, so mention this
    print("\n>> Request recent page logs:")
    print("Cannot access server-side logs from the client side due to security restrictions.")
    output_lines.append(">> Request recent page logs:")
    output_lines.append("Cannot access server-side logs from the client side due to security restrictions.\n")

    # Determine web page legitimacy (very basic check)
    print("\n>> Determine web page legitimacy / Detect phishing link:")
    output_lines.append(">> Determine web page legitimacy / Detect phishing link:")
    is_suspicious = False
    phishing_patterns = [
        r"(account|login|secure|bank|update)[^/]*\.[^/]*\.[a-z]{2,}",
        r"(free|bonus|gift|prize|claim)[^/]*\.[^/]*\.[a-z]{2,}",
        r"[0-9]{1,3}(?:\.[0-9]{1,3}){3}",  # IP in URL
        r"@",
        r"-security",
        r"-verify",
        r"-paypal",
        r"servicenow-sites"
    ]
    for pattern in phishing_patterns:
        if re.search(pattern, url, re.IGNORECASE):
            is_suspicious = True
            break

    if is_suspicious or "phish" in url.lower():
        print("Warning: This URL may be suspicious or a phishing attempt!")
        output_lines.append("Warning: This URL may be suspicious or a phishing attempt!")
    else:
        print("No obvious signs of phishing detected (but always verify manually).")
        output_lines.append("No obvious signs of phishing detected (but always verify manually).")

except Exception as e:
    print(f"Error fetching the web page: {e}")
    output_lines.append(f"Error fetching the web page: {e}\n")

# Write full output to a txt file
with open("output.txt", "w", encoding="utf-8") as f:
    for line in output_lines:
        f.write(line)
        if not line.endswith("\n"):
            f.write("\n")

print("\nDone! The full report is saved in output.txt")