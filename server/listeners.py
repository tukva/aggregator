from common.rest_client.base_client_betting_data import BaseClientBettingData

from engine import Engine


client = BaseClientBettingData()


async def acquire_con(app, loop):
    await Engine.init()


async def parse_real_teams(app, loop):
    await client.put_all_links(params='real_teams')


async def close_con(app, loop):
    await Engine.close()
