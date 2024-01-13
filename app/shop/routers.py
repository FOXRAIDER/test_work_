from fastapi import APIRouter


router = APIRouter(
    tags=["shop"],
    prefix="/items",
    dependencies=[],
)


@router.get(
    "/",
    summary="Get all items",
)
async def get_all(self):
    pass
