import flask
import scraper

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/refresh', methods=['POST'])
def home():
    try:
        scraper.scrape()
        return 'Ran Successfully'
    except Exception as e:
        if (app.config['DEBUG'] == True):
            return str(e)
        else:
            return 'Error Encountered'


app.run()
