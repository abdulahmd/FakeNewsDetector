from flask import Flask, request, render_template, redirect, url_for, flash
import os

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

