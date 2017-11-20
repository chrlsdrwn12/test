#!flask/bin/python
from application import app
app.run(
    host="0.0.0.0",
    port=int("8500"),
    debug=True
)