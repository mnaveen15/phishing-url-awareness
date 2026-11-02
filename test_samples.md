# Test Results

Python version used: 3.13+  
Operating system: Android / Pydroid 3 or any Python 3.10+ environment  
Date: 2026-11-02

The five sample strings below are the exact workbook samples. The expected results follow the workbook. The actual-result wording below records the behavior of this completed program.

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs | No listed warning signs found. This does NOT prove safety. | PASS |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | Uses an IP address instead of a familiar domain; Uses HTTP. | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | Contains an @ symbol; Uses HTTP. | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Contains many hostname segments/subdomains. | PASS |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Contains a punycode-style hostname. | PASS |

## Notes

I learned that URL warning signs are useful clues rather than proof that a link is malicious. I also understood that HTTPS alone does not prove that a website is trustworthy.

The most useful improvement was adding explanations for each warning, because it makes the output easier for a beginner to understand.
