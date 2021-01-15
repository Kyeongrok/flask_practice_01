from flaskblog import app
from flask import render_template, flash, redirect, url_for

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
