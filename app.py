import os
from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)

# ── Main study guide ──────────────────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html")

# ── Health check (Railway uses this) ─────────────────────────────────────────
@app.route("/health")
def health():
    return jsonify({"status": "ok", "app": "CV Anatomy Anesthesia Study Guide"}), 200

# ── Static file fallback ──────────────────────────────────────────────────────
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

# ── 404 handler ───────────────────────────────────────────────────────────────
@app.errorhandler(404)
def not_found(e):
    return render_template("index.html"), 200  # SPA fallback

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
