from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from database.db_manager import base_manager
from groups import router as group_router
from settings import SCRIPTS_PATH

app = FastAPI()

app.include_router(group_router, prefix="/groups")


@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_PATH)
    uvicorn.run(app="start_server:app", host="0.0.0.0",  port=8000, reload=True)


