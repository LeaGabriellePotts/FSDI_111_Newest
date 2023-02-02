from flask import Flask         # From the flask module import the Flask class.


app = Flask(__name__)             # Create an instance of the Flask class into the app variable (now an object



@app.get("/")                   # Flask decorator that creates routes.
def index():                    # Flask calls these "view functions."
    me = {                      # Python dictionary with key/value pairs.
        "first_name": "TopFun",    
        "last_name": "USA",     
        "hobbies": "Skiing",    
        "is_active": True
    }
    return me                   # When a view function returns a dict.
                                # Flask automatically converts it to JSON.