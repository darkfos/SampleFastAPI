#global directives
from fastapi import FastAPI

#Import views
from views.items.views import item_router as itm_r
from views.calculator.views import calc_router as clc_r

import uvicorn
import random

#Application
app: FastAPI = FastAPI(title="MyApplication")



#Load routers
app.include_router(
    itm_r,
    prefix="/api", #Prefix for rouyter
    )

app.include_router(
    clc_r,
    prefix="/api"
)

#Base api services

@app.get("/hi/")
def get_message_by_hi(name: str, surname: str):
    return {"message": "Hi {} {}!".format(name, surname)}

if __name__ == "__main__":
    #Run application
    # Other command to start -> uvicorn main:app --reload | main - python module and app us application.
    uvicorn.run(app=app)