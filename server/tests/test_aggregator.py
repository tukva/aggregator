from unittest import mock

import pytest
from common.rest_client.base_client_betting_data import BaseClientBettingData


@pytest.mark.aggregator
async def test_aggregator(test_cli, mock_resp_status_200, mock_resp_status_404,  mock_resp_real_teams):
    with mock.patch.object(BaseClientBettingData, 'get_all_links', return_value=mock_resp_real_teams):
        with mock.patch.object(BaseClientBettingData, 'get_by_link') as mock_get_by_link:
            mock_get_by_link.side_effect = [mock_resp_status_200, mock_resp_status_404]
            resp = await test_cli.get('/aggregate')

            assert resp.status == 200
            assert await resp.json() == {'1': [{'name': 'chelsea'}, {'name': 'manchester united'}],
                                         'real_teams': [{'name': 'FC Chelsea'}, {'name': 'Liverpool'}]}

        with mock.patch.object(BaseClientBettingData, 'get_by_link') as mock_get_by_link:
            mock_get_by_link.side_effect = [mock_resp_status_200, mock_resp_status_404]
            resp = await test_cli.get('/aggregate?team=FC Chelsea')

            assert resp.status == 200
            assert await resp.json() == {'1': ['chelsea', 'manchester united'],
                                         'real_teams': 'FC Chelsea'}


@pytest.mark.aggregator
async def test_aggregator_by_link(test_cli, mock_resp_teams, mock_resp_real_teams):
    with mock.patch.object(BaseClientBettingData, 'get_by_link', return_value=mock_resp_teams):
        with mock.patch.object(BaseClientBettingData, 'get_all_links', return_value=mock_resp_real_teams):
            resp = await test_cli.get('/aggregate/1')

            assert resp.status == 200
            assert await resp.json() == {'1': [{'name': 'chelsea'}, {'name': 'manchester united'}],
                                         'real_teams': [{'name': 'FC Chelsea'}, {'name': 'Liverpool'}]}

            resp = await test_cli.get('/aggregate/1/?team=FC Chelsea')

            assert resp.status == 200
            assert await resp.json() == {'1': ['chelsea', 'manchester united'],
                                         'real_teams': 'FC Chelsea'}
