from app.utils import Router


router = Router()


@router.post('/nbc')
def login() -> str:

    return "Hi there!"
