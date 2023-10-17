from flask import Flask, jsonify, make_response, render_template, render_template_string, url_for, flash, redirect, request
app = Flask(__name__)

@app.route('/')
def bonjour():
    message = {"message": "Bonjour"}
    return jsonify(message)

if __name__ == '__main__':
    # Lancez l'application Flask en mode développement
    app.run(host="0.0.0.0",port=5000,debug=True)