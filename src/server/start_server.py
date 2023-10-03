import settings
from database.db_manager import base_manager

from fastapi import FastAPI
import uvicorn
from groups.routers import router as group_router

app = FastAPI()

app.include_router(group_router, prefix='/groups')

if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(settings.SCRIPTS_PATH)

    uvicorn.run(app=app, host='0.0.0.0', port=8001)



