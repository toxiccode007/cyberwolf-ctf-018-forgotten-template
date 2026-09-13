# CyberWolf CTF #018 — The Forgotten Template

Category: WEB
Difficulty: HARD
Points: 250
Flag: `CYBERWOLF{forgotten_template_executed}`

## Deployment
Render Runtime: Docker
Branch: main
Region: Ohio
Instance: Free

## Author note
The challenge demonstrates a controlled server-side template evaluation concept. The public application exposes document preview functionality and a help page. The intended student investigation is to identify the legacy renderer and test whether user-controlled preview data is evaluated as a template.

The application is deliberately isolated and does not provide operating-system command execution. The intended objective is to retrieve the CTF flag only.
