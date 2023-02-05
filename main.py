from fastapi import FastAPI
import Models.Order
from config import engine
import Routers.routes
import uvicorn
from starlette.responses import RedirectResponse

Models.Order.Base.metadata.create_all(bind = engine)
app = FastAPI()

@app.get('/')
async def Home():
    return RedirectResponse(url = "/docs")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6969)

app.include_router(Routers.routes.router,prefix="/api",tags=["order"])