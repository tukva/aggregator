import pytest
from sanic import Sanic

from routes import add_routes
from engine import Engine


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: smoke tests")
    config.addinivalue_line("markers", "aggregator: aggregator tests")


@pytest.fixture
def test_cli(loop, sanic_client):
    app = Sanic()
    add_routes(app)
    return loop.run_until_complete(sanic_client(app))


@pytest.fixture
async def connection():
    await Engine.init()

    yield

    await Engine.close()
