from stdmgmt import app
from stdmgmt.models import db

app.app_context().push()
db.create_all()
