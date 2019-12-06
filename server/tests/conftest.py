import asyncio
from unittest import mock

import pytest
from sanic import Sanic
from common.rest_client.base_client_betting_data import BaseClientBettingData

from routes import add_routes
from engine import Engine


def pytest_configure(config):
    config.addinivalue_line("markers", "smoke: smoke tests")
    config.addinivalue_line("markers", "aggregator: aggregator tests")


@pytest.fixture
def test_cli(loop, sanic_client):
    app = Sanic()
    add_routes(app)

    class Response:
        json = {"Ok"}

    future = asyncio.Future()
    future.set_result(Response())

    with mock.patch.object(BaseClientBettingData, 'put_all_links', return_value=future):
        return loop.run_until_complete(sanic_client(app))


@pytest.fixture
async def connection():
    await Engine.init()

    yield

    await Engine.close()


@pytest.fixture
async def mock_resp_teams(test_cli):
    class Response:
        json = [{"name": "chelsea"}, {"name": "manchester united"}]

    future = asyncio.Future()
    future.set_result(Response())
    return future


@pytest.fixture
async def mock_resp_real_teams(test_cli):
    class Response:
        json = [{"name": "FC Chelsea"}, {"name": "Liverpool"}]

    future = asyncio.Future()
    future.set_result(Response())
    return future


@pytest.fixture
async def mock_resp_status_200(test_cli):
    class Response:
        json = [{"name": "chelsea"}, {"name": "manchester united"}]
        status = 200

    future = asyncio.Future()
    future.set_result(Response())
    return future


@pytest.fixture
async def mock_resp_status_404(test_cli):
    class Response:
        status = 404

    future = asyncio.Future()
    future.set_result(Response())
    return future
