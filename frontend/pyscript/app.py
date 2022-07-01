import json
import asyncio
from pyodide.http import pyfetch
from pyodide import JsException

async def GetTasks():
    response = await pyfetch(
        url="http://127.0.0.1:8000/",
        method="GET",
        headers={"Content-Type": "application/json"},
    )
    if response.ok:
        data = await response.json()
  
        return data
