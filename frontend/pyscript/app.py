import json
import asyncio
from pyodide.http import pyfetch
from pyodide import JsException,create_proxy
import js

async def GetTasks():
    response = await pyfetch(
        url="http://127.0.0.1:8000/",
        method="GET",
        headers={"Content-Type": "application/json"},
    )
    if response.ok:
        data = await response.json()
        return data

async def delete_onclick(id):
    id = id
    print(id)
    response = await pyfetch(
        url="http://127.0.0.1:8000/delete",
        method="POST",
        headers={"Content-Type": "application/json"},
    )
    return response  

