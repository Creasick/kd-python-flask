from flask import Flask, request, make_response
from waitress import serve

app = Flask(__name__)
koders = [{"name": "mike"}, {"name": "charles"}, {"name": "Pedro"}, {"name": "Luis"}]


@app.route("/")
def hola_mundo():
  return {"message": "hola mundo"}


@app.route("/koders")
def get_koders():
  return {"koders": koders}


@app.route("/koders", methods=["POST"])
def create_koder():
  data = request.json
  koders.append({"name": data["name"]})
  return {"message": "Koder created", "Koders": koders}


@app.route("/koders/<name>", methods=["DELETE"])
def delete_koder(name):
  if {"name": name} in koders:
    koders.remove({"name": name})
    return {"message": "Koder deleted", "Koders": koders}
  else:
    return make_response({"message": f"Koder {name} don't exists"}, 404)


if __name__ == "__main__":
  # app.run()
  serve(app, host="127.0.0.1", port=8000)
