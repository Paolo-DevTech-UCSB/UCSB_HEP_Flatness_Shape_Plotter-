import asyncio, asyncpg
import PGConnect
import numpy as np


async def main():
    Selected_File = await PG_Select()
    Data = await PGConnect.get_data(Selected_File)
    # Combine into list of (x, y, z) tuples
    x_points = Data[2]; y_points = Data[3]; z_points = Data[4]
    points = list(zip(x_points, y_points, z_points))

    # Print the result
    for point in points:
        print(point)

    #print(points_dist)

    

async def PG_Select():
    List = await PGConnect.get_names()
    for name in List:
        print(name)

    print("Choose a name by number:")
    for i, name in enumerate(List, start=1):
        print(f"{i}. {name}")

    # Ask user for input
    choice = int(input("Enter the number of the name you want: "))

    # Validate and return the selected name
    if 1 <= choice <= len(List):
        selected_name = List[choice - 1]
        print(f"You selected: {selected_name}")
    else:
        print("Invalid choice. Please enter a number from the list.")

    return selected_name

    

asyncio.run(main())
