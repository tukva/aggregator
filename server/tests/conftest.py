import asyncio

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


@pytest.fixture
async def mock_resp_teams(test_cli):
    future = asyncio.Future()
    future.set_result([{"name": "chelsea", "link_id": 1}, {"name": "manchester united", "link_id": 1}])
    return future


@pytest.fixture
async def mock_resp_real_teams(test_cli):
    future = asyncio.Future()
    future.set_result([{"name": "FC Chelsea"}, {"name": "Liverpool"}])
    return future
