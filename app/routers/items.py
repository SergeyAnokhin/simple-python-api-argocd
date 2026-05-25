from fastapi import APIRouter, HTTPException

router = APIRouter()

ITEMS = [
    {"id": 1, "name": "Widget"},
    {"id": 2, "name": "Gadget"},
    {"id": 3, "name": "Doohickey"},
]


@router.get("")
def list_items():
    return ITEMS


@router.get("/{item_id}")
def get_item(item_id: int):
    for item in ITEMS:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
