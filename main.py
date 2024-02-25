#global directives
from fastapi import FastAPI

#Import views
from views.items.views import item_router as itm_r

import uvicorn
import random

#Application
app: FastAPI = FastAPI()



#Load routers
app.include_router(
    itm_r,
    prefix="/api" #Prefix for rouyter
    )

if __name__ == "__main__":
    #Run application
    # Other command to start -> uvicorn main:app --reload | main - python module and app us application.
    uvicorn.run(app=app)