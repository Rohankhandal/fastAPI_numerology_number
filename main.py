from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserInput(BaseModel):
    name: str


@app.post("/numerology")
def numerology(data: UserInput):
    total = 0

    for ch in data.name.lower():
        if ch.isalpha():
            total += ord(ch) - 96

    while total > 9:
        total = sum(int(d) for d in str(total))

    return {
        "name": data.name,
        "numerology_number": total
    }




# =====================================================================

# using get method 

# from fastapi import FastAPI

# app = FastAPI()

# # Request (GET)
# # /numerology?name=saurabh

# # Response
# # {
# #   "name": "saurabh",
# #   "numerology_number": 7
# # }

# @app.get("/numerology")
# def numerology(name: str):
#     total = 0

#     for ch in name.lower():
#         if ch.isalpha():
#             total += ord(ch) - 96

#     while total > 9:
#         total = sum(int(d) for d in str(total))

#     return {
#         "name": name,
#         "numerology_number": total
#     }

# =====================================================================
