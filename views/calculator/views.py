from fastapi import APIRouter, Depends, Body, Header
from typing import Annotated

from .schemas import DataCalc

# APIRouter for calculator
calc_router: APIRouter = APIRouter(prefix="/calc", tags=["Calculator"])


@calc_router.get("/sum")
def sum_numbers(params_for_sm: DataCalc = Depends()):
    return {
        **params_for_sm.model_dump(),
        "result": params_for_sm.number_1 + params_for_sm.number_2
    }

@calc_router.post("/mul")
def mul_numbers(
    params_to_mul: Annotated[DataCalc, Body()], 
    action: Annotated[bool, Header()] = False,
):
    if action == True:
        return {
            **params_to_mul.model_dump(),
            "result": params_to_mul.number_1 ** params_to_mul.number_2
        }
    return {
        **params_to_mul.model_dump(),
        "result": params_to_mul.number_1 * params_to_mul.number_2
    }