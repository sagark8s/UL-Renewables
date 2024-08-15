from fastapi import APIRouter

import Zipher.routes as zipher
import Windcube.routes as wind_cube

api_router = APIRouter()
api_router.include_router(zipher.router, tags=["Zipher"], prefix="/zipher")
api_router.include_router(wind_cube.router, tags=["Windcube"], prefix="/windcube")
