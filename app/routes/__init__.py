from fastapi import APIRouter

from .nbc import router as nbcRouter


router = APIRouter()


@router.get('/ping')
async def read_root() -> str:
    return 'pong'


router.include_router(nbcRouter)
