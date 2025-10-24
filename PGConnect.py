
import asyncpg
import asyncio
import json
import os

async def get_data(Selected_Data):
    # Load config from desktop  
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "DBconfig.json")
    with open(desktop_path, "r") as f:
        config = json.load(f)

    # Connect using loaded config
    conn = await asyncpg.connect(**config)

    # Query the table
    rows = await conn.fetch('SELECT module_name, flatness, x_points, y_points, z_points FROM module_inspect')

    Names_List = []

    for row in rows:
        if row['module_name'] == Selected_Data:
            Data = row
    

    await conn.close()

    return Data



async def get_names():
    # Load config from desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "DBconfig.json")
    with open(desktop_path, "r") as f:
        config = json.load(f)

    # Connect using loaded config
    conn = await asyncpg.connect(**config)

    # Query the table
    rows = await conn.fetch('SELECT module_name, flatness, x_points, y_points, z_points FROM module_inspect')

    Names_List = []

    for row in rows:
        x_points = row['x_points']
        y_points = row['y_points']
        z_points = row['z_points']
        if not any(sub in row['module_name'] for sub in ['dum', 'run', 'dry', 'Dry', 'Run']): 
            Names_List.append(row['module_name'])

    

    await conn.close()

    return Names_List


asyncio.run(get_names())
