from controller.recs_controller import RecsController
from model.recs_request import RecsRequest
from model.recs_response import RecsResponse


class RCNNRecsController(RecsController):
    def predict_cells(self, rec_request: RecsRequest) -> RecsResponse:
        pass