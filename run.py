from stdmgmt import app
import json

appProfile = {}

with open("appProfile.json") as f:
    appProfile = json.loads(f.read())
    app.config['adminPw'] = appProfile["adminPw"]

if __name__ == "__main__":
    app.run(debug=True)
