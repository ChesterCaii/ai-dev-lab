from flask import redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
from . import app

# Create a GitHub OAuth blueprint
github_bp = make_github_blueprint(client_id="GITHUB_CLIENT_ID", client_secret="GITHUB_CLIENT_SECRET")
app.register_blueprint(github_bp, url_prefix="/login")

@app.route("/github")
def github_login():
    if not github.authorized:
        return redirect(url_for("github.login"))
    resp = github.get("/user")
    assert resp.ok, resp.text
    return "You are @{login} on GitHub".format(login=resp.json()["login"]) 