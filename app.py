from fastapi import FastAPI, Path

app = FastAPI()

inventory = {1: {"name": "Hair Tie", "price": 30.00, "type": "Garnet"}}


# Create endpoint
@app.get("/get-item/{item_id}")
def get_item(
    item_id: int = Path(description="The ID of the item you'd like to view", gt=0, lt=2)
):
    return inventory[item_id]


@app.get("/get-by-name")
def get_item(name: str):
    for item_id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data": "Not found"}
