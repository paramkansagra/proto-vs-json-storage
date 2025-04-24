from typing import List, Dict, AnyStr

from json.encoder import JSONEncoder

data: List[Dict[int, AnyStr]] = [
    {"id": 1, "name": "Param", "salary": 1000},
    {"id": 2, "name": "Jayesh", "salary": 2000},
    {"id": 3, "name": "Mayuri", "salary": 3000},
    {"id": 4, "name": "Pari", "salary": 4000},
]

encoded = JSONEncoder().encode(data)

file = open("json_data.json", "w+")
file.write(encoded)
file.close()

# it is taking 177 bytes on my disk