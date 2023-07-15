from flask import Flask, render_template, url_for, session, abort, redirect
from authlib.integrations.flask_client import OAuth
import json

app = Flask(__name__)

appConf = {
  "OAUTH2_CLIENT_ID": "password-client",
  "OAUTH2_CLIENT_SECRET": "XG1IO71uGtfE1c0fOBzmyDL9U4Xr8pbb",
  "OAUTH2_ISSUER": "http://192.168.187.138:8080/realms/PASSWORD",
  "FLASK_SECRET": "ALongRandomlyGeneratedString",
  "FLASK_PORT": 3000
}

app.secret_key = appConf.get("FLASK_SECRET")

oauth = OAuth(app)
oauth.register(
    "auth0",
    client_id=appConf.get("OAUTH2_CLIENT_ID"),
    client_secret=appConf.get("OAUTH2_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'{appConf.get("OAUTH2_ISSUER")}/.well-known/openid-configuration',
)

@app.route("/")
def home():
    return render_template("home.html", session=session.get("user"),
                            pretty=json.dumps(session.get("user"), indent=4))

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect(url_for("home"))

@app.route("/login")
def login():
    if "user" in session:
        abort(404)
    return oauth.auth0.authorize_redirect(redirect_uri=url_for("callback", _external=True)
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
