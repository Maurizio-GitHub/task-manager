# To use environment variables within this file, we need to import the 'app'
# variable created within our 'taskmanager' package, defined into __init__.py:
import os
from taskmanager import app


# To run our application, we need to tell our 'app' how and where. We need
# to check that the __name__ class is equal to the default "__main__" string.
# If matching, we need our app running with three arguments:
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
