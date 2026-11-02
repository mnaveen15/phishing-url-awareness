Test Samples

Sample 1

URL: "https://www.example.com/login"

Expected: No listed warning signs.

Result: PASS

---

Sample 2

URL: "http://192.0.2.10/account"

Expected: IP address and HTTP warning.

Result: PASS

---

Sample 3

URL: "http://example.com@sample.invalid/login"

Expected: "@" symbol and HTTP warning.

Result: PASS

---

Sample 4

URL: "https://a.b.c.d.e.example.invalid/path"

Expected: Too many hostname segments warning.

Result: PASS

---

Sample 5

URL: "https://xn--example.invalid/"

Expected: Punycode warning.

Result: PASS

---

Test Summary

All 5 required sample URLs were tested successfully.

Result: 5/5 PASS
