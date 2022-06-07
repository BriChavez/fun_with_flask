from flask import Flask

app = Flask(__name__)


@app.route("/")
# def index():
#         print("you did it!")
#         """    # this function defines what should be executed if the 
#             defined URL endpoint is requested by a user""" 
#             #    the naming of index is only a convention
    

def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    celsius = input("Celsius: ")
    print("Fahrenheit:", fahrenheit_from(celsius))

# if __name__ == "__main__":
#         app.run(host="127.0.0.1", port=8080, debug=True)

"""        These two lines tell Python to start Flask’s development 
        server when the script is executed from the command line. 
        It’ll be used only when you run the script locally. 
        When you deploy the code to Google App Engine, a professional web server process, 
        such as Gunicorn, will serve the app instead. 
        You won’t need to change anything to make this happen."""