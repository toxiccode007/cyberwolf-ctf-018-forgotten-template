# CyberWolf CTF #018 — The Forgotten Template (HARD)

Category: WEB
Difficulty: HARD
Points: 250
Flag: `CYBERWOLF{forgotten_template_executed}`

## Intended solve
1. Open the application.
2. Explore `/help`.
3. Discover the `note` parameter used by the legacy preview renderer.
4. Test whether the note is interpreted as a server-side template.
5. Use the exposed `secret` template variable to retrieve the CTF flag.

The challenge intentionally demonstrates a controlled Jinja server-side template injection (SSTI) issue. It does not provide OS command execution or access to the host system.

A simple validation payload is:
`{{7*7}}`

Once template evaluation is confirmed, the intended CTF secret variable is:
`{{secret}}`

## Render
Runtime: Docker
Branch: main
Region: Ohio
Instance: Free
