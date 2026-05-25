from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    id: int
    name: str


ITEMS: list[Item] = [
    Item(id=1, name="Widget"),
    Item(id=2, name="Gadget"),
    Item(id=3, name="Doohickey"),
]


@router.get(
    "",
    response_model=list[Item],
    summary="Список всех items",
)
def list_items():
    """Возвращает полный список доступных объектов Item."""
    return ITEMS


@router.get(
    "/{item_id}",
    response_model=Item,
    summary="Получить item по ID",
    responses={404: {"description": "Item не найден"}},
)
def get_item(item_id: int):
    """Возвращает один объект Item по его числовому **id**.

    - **item_id**: целое число от 1 до 3
    """
    for item in ITEMS:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
