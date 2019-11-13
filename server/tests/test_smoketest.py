import pytest

from engine import Connection, Engine


@pytest.mark.smoke
async def test_acquire_connection():
    await Engine.init()
    async with Connection():
        assert True
    await Engine.close()


@pytest.mark.smoke
async def test_close_connection():
    await Engine.init()
    await Engine.close()
    try:
        async with Connection():
            assert False
    except RuntimeError:
        assert True


@pytest.mark.smoke
async def test_server(test_cli):
    await test_cli.get('/real-team')
    assert True
