from app.services import classifier
from app.schemas.classifier import GetPerceptionRequest, GetPerceptionResponse
from app.utils import Router


router = Router()


@router.post('/v1/get-perception')
def get_perception(payload: GetPerceptionRequest) -> GetPerceptionResponse:

    perception, detail = classifier.get_perception(payload.input)

    return GetPerceptionResponse(perception=perception, detail=detail)
