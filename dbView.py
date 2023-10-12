from stdmgmt import app, db
from stdmgmt.models import Student


app.app_context().push()

s = Student.query.all()
for i in s:
    print(i.id, i.picture)
