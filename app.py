import os

from flask import Flask

app = Flask(__name__)

if __name__ == "__main__":
    from views.admin import *
    from views.league import *
    from views.stat import *
    from views.week import *
    from views.year import *

    if os.getenv("TEST_ENVIRONMENT") == "True":
        app.run(debug=True)
    else:
        app.run(host="0.0.0.0", port=80)
