# Builds worker/dist.js: the worker code plus the website, so Cloudflare serves both.
import json, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
src = (root / "worker" / "worker.js").read_text()
html = (root / "index.html").read_text()
prompt = (root / "system-prompt.md").read_text()
out = src + "\nconst SITE_HTML = " + json.dumps(html) + ";\nconst SITE_PROMPT = " + json.dumps(prompt) + ";\n"
(root / "worker" / "dist.js").write_text(out)
print("dist.js", len(out), "bytes")
