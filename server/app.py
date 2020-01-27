from sanic import Sanic
from sanic_cors import CORS

from config import AGGREGATOR_API_PORT, AGGREGATOR_API_HOST
from routes import add_routes

app = Sanic(name=__name__)
cors = CORS(app, automatic_options=True)
add_routes(app)

if __name__ == '__main__':
    app.run(host=AGGREGATOR_API_HOST, port=AGGREGATOR_API_PORT)
