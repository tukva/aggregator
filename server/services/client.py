from common.rest_client import BaseClient


class BaseClientParser(BaseClient):
    def __init__(self, host, port, headers=None):
        super().__init__(host, port, headers=headers)

        self._api_uri = {
            'all_teams': 'parse-links/teams',
            'teams_by_link': 'parse-links/{link_id}/teams',
            'real_teams': 'real-teams',
        }

    async def get_all_teams(self):
        url = self._api_uri['all_teams']
        async with await super().get(url, cookies=self._cookies, params=None) as response:
            return await response.json()

    async def get_teams_by_link(self, link_id):
        url = self._api_uri['teams_by_link'].format(link_id=link_id)
        async with await super().get(url, cookies=self._cookies, params=None) as response:
            if response.status == 404:
                return {"status": response.status}
            return {"json": await response.json(), "status": response.status}

    async def put_teams_by_link(self, link_id):
        url = self._api_uri['teams_by_link'].format(link_id=link_id)
        async with await super().put(url, cookies=self._cookies, params=None) as response:
            return await response.text()

    async def delete_teams_by_link(self, link_id):
        url = self._api_uri['teams_by_link'].format(link_id=link_id)
        async with await super().delete(url, cookies=self._cookies, params=None) as response:
            return await response.text()

    async def get_real_teams(self):
        url = self._api_uri['real_teams']
        async with await super().get(url, cookies=self._cookies, params=None) as response:
            return await response.json()

    async def put_real_teams(self):
        url = self._api_uri['real_teams']
        async with await super().put(url, cookies=self._cookies, params=None) as response:
            return await response.text()
