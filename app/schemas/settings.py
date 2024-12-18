from pydantic import BaseModel

class CalculationRequest(BaseModel):
    a: int
    b: int
