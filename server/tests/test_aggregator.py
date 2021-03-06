from http import HTTPStatus
from unittest import mock

import pytest
from common.rest_client.base_client_betting_data import BaseClientBettingData


@pytest.mark.aggregator
async def test_aggregator(test_cli, mock_resp_teams, mock_resp_real_teams):
    with mock.patch.object(BaseClientBettingData, 'get_real_teams', return_value=mock_resp_real_teams):
        with mock.patch.object(BaseClientBettingData, 'get_teams', return_value=mock_resp_teams):
            resp = await test_cli.get('/aggregate')

            assert resp.status == HTTPStatus.OK
            assert await resp.json() == {'teams': [{'name': 'chelsea', 'link_id': 1},
                                               {'name': 'manchester united', 'link_id': 1}],
                                         'real_teams': [{'name': 'FC Chelsea'}, {'name': 'Liverpool'}]}

            resp = await test_cli.get('/aggregate?team=FC Chelsea')

            assert resp.status == HTTPStatus.OK
            assert await resp.json() == {'teams': ['chelsea', 'manchester united'],
                                         'real_teams': 'FC Chelsea'}


@pytest.mark.aggregator
async def test_aggregator_by_link(test_cli, mock_resp_teams, mock_resp_real_teams):
    with mock.patch.object(BaseClientBettingData, 'get_teams', return_value=mock_resp_teams):
        with mock.patch.object(BaseClientBettingData, 'get_real_teams', return_value=mock_resp_real_teams):
            resp = await test_cli.get('/aggregate?where=link_id:eq:1')

            assert resp.status == HTTPStatus.OK
            assert await resp.json() == {'teams': [{'name': 'chelsea', 'link_id': 1},
                                               {'name': 'manchester united', 'link_id': 1}],
                                         'real_teams': [{'name': 'FC Chelsea'}, {'name': 'Liverpool'}]}

            resp = await test_cli.get('/aggregate/?team=FC Chelsea&where=link_id:eq:1')

            assert resp.status == HTTPStatus.OK
            assert await resp.json() == {'teams': ['chelsea', 'manchester united'],
                                         'real_teams': 'FC Chelsea'}
