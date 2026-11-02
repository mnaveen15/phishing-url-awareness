#!/usr/bin/env python3
"""
EWB Courses - Cybersecurity Mini Project
Phishing URL Awareness Checker

Defensive learning tool: analyzes URL text only.
It never opens or visits the URL.
"""

from ipaddress import ip_address
from urllib.parse import urlparse


REASONS = {
    "at": "The @ symbol can hide the real destination because text before @ may be treated as user information.",
    "long": "Very long URLs can hide the important destination details far to the right.",
    "ip": "Uses an IP address instead of a familiar domain.",
    "segments": "Many hostname segments/subdomains can make a link look more official than it is.",
    "punycode": "Punycode-style hostnames can represent look-alike international characters.",
    "http": "Uses HTTP. HTTPS alone does not prove trust, but HTTP does not provide encrypted transport.",
}


def _is_ip_hostname(hostname: str) -> bool:
    if not hostname:
        return False
    try:
        ip_address(hostname)
        return True
    except ValueError:
        return False


def inspect_url(raw_url: str) -> list[str]:
    """Return warning messages for one URL string."""
    raw_url = raw_url.strip()
    if not raw_url:
        return ["Please enter a URL."]

    candidate = raw_url if "://" in raw_url else "http://" + raw_url

    try:
        parsed = urlparse(candidate)
    except ValueError:
        return ["This text is not a valid URL format."]

    if not parsed.hostname:
        return ["This text is not a valid URL format."]

    findings = []

    if "@" in raw_url:
        findings.append("Contains an @ symbol; inspect carefully.")

    if len(raw_url) > 100:
        findings.append("URL is longer than 100 characters.")

    if _is_ip_hostname(parsed.hostname):
        findings.append(REASONS["ip"])

    hostname = parsed.hostname
    segments = [part for part in hostname.split(".") if part]
    if len(segments) >= 5:
        findings.append("Contains many hostname segments/subdomains.")

    if "xn--" in hostname.lower():
        findings.append("Contains a punycode-style hostname.")

    if parsed.scheme.lower() == "http":
        findings.append("Uses HTTP. HTTPS alone does not prove trust.")

    return findings


def explain_findings(findings: list[str]) -> list[str]:
    """Return short explanations for the warnings."""
    explanations = []
    for item in findings:
        if "@" in item:
            explanations.append(REASONS["at"])
        elif "longer than 100" in item:
            explanations.append(REASONS["long"])
        elif "IP address" in item:
            explanations.append(REASONS["ip"])
        elif "many hostname" in item.lower():
            explanations.append(REASONS["segments"])
        elif "punycode" in item.lower():
            explanations.append(REASONS["punycode"])
        elif "Uses HTTP" in item:
            explanations.append(REASONS["http"])
    return explanations


def print_result(raw_url: str) -> None:
    findings = inspect_url(raw_url)

    print("\nURL:", raw_url)
    print("Result:")

    if len(findings) == 1 and findings[0] in {
        "Please enter a URL.",
        "This text is not a valid URL format.",
    }:
        print("- " + findings[0])
        return

    if not findings:
        print("- No listed warning signs found. This does NOT prove safety.")
        return

    for item in findings:
        print("- " + item)

    print("\nWhy these were flagged:")
    for reason in explain_findings(findings):
        print("- " + reason)

    print(f"\nREVIEW CAREFULLY: {len(findings)} warning sign(s) found.")


def main() -> None:
    print("=" * 62)
    print("        EWB PHISHING URL AWARENESS CHECKER")
    print("=" * 62)
    print("Defensive learning tool: URL text is analyzed locally.")
    print("The program never visits or opens the URL.")
    print("Enter one URL, or paste multiple URLs separated by commas.")
    print("Type 'q' to quit.")

    while True:
        raw = input("\nURL(s): ").strip()

        if raw.lower() in {"q", "quit", "exit"}:
            print("Goodbye.")
            break

        if not raw:
            print("Please enter a URL.")
            continue

        # Improvement 1: multiple URL input without restarting.
        urls = [item.strip() for item in raw.split(",") if item.strip()]

        for url in urls:
            print_result(url)


if __name__ == "__main__":
    main()
