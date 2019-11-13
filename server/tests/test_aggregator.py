import pytest


@pytest.mark.aggregator
async def test_aggregator(test_cli):
    resp = await test_cli.get('/aggregator')

    assert resp.status == 200
    assert len(await resp.json()) == 5

    resp = await test_cli.get('/aggregator/?team=chelsea')
    resp_json = await resp.json()
    assert resp.status == 200
    assert len(resp_json) == 5
    assert resp_json["real_team"] == 'chelsea'
    assert len(resp_json["1"]) <= 10


@pytest.mark.aggregator
async def test_aggregator_by_link(test_cli):
    resp = await test_cli.get('/aggregator/1')

    assert resp.status == 200
    assert len(await resp.json()) == 2

    resp = await test_cli.get('/aggregator/1/?team=chelsea')
    resp_json = await resp.json()
    assert resp.status == 200
    assert len(resp_json) == 2
    assert resp_json["real_team"] == 'chelsea'
    assert len(resp_json["1"]) <= 10
