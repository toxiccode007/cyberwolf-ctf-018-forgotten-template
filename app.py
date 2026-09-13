from flask import Flask, render_template, request, render_template_string
import os

app = Flask(__name__)

FLAG = "CYBERWOLF{forgotten_template_executed}"

DOCUMENTS = {
    "security-report": {
        "title": "Security Review",
        "body": "Quarterly security review — no public incidents recorded."
    },
    "migration-notes": {
        "title": "Migration Notes",
        "body": "Legacy preview rendering was retained for compatibility."
    },
    "archive-summary": {
        "title": "Archive Summary",
        "body": "Historical documents have been moved to the new archive."
    }
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/preview")
def preview():
    name = request.args.get("name", "security-report")
    note = request.args.get("note", "")

    document = DOCUMENTS.get(name)
    if not document:
        return "Document not found.", 404

    # Intentionally vulnerable CTF behavior:
    # the legacy renderer concatenates the user-controlled note into
    # the server-side Jinja template before rendering it.
    template = f"""
    <html>
    <head><title>{document["title"]}</title>
    <style>
      body{{background:#05080d;color:#dceeff;font-family:Arial;padding:45px}}
      article{{max-width:760px;margin:auto;background:#08111a;border:1px solid #1d4058;padding:35px}}
      h1{{color:#39c5ff}}p{{color:#9bb2c5;line-height:1.8}}
      .note{{font-family:monospace;color:#72d8ff;border:1px solid #18384d;padding:15px}}
    </style></head>
    <body><article>
    <div class="note">CYBERWOLF DOCUMENT PREVIEW</div>
    <h1>{document["title"]}</h1>
    <p>{document["body"]}</p>
    <p class="note">{note}</p>
    </article></body></html>
    """
    # The secret is deliberately available as a template variable.
    # Students should retrieve only the CTF flag.
    return render_template_string(template, secret=FLAG)

@app.route("/help")
def help_page():
    return """<html><body style="font-family:Arial;background:#05080d;color:#dceeff;padding:45px">
<h2>Preview Help</h2>
<p>The legacy preview service accepts a document name through the <b>name</b> parameter.</p>
<p>Example: <code>/preview?name=security-report</code></p>
<p>Optional analyst notes can be supplied with the <b>note</b> parameter.</p>
<p>Legacy migration note: the old renderer used a server-side template for document previews.</p>
</body></html>"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",5000)))
