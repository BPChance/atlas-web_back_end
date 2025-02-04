from flask import Flask, request
from flask_babel import Babel, _

app = Flask(__name__)

# configure languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

def get_locale():
    """ checks Accept-Language header to determine best language match """
    return request.accept_languages.best_match(['en', 'fr'])

# initialize Babel
babel = Babel(app, locale_selector=get_locale)

@app.route('/')
def index():
    """ returns message based on the selected locale """
    return _("Hello, World!")


if __name__ == "__main__":
    app.run(debug=True)
