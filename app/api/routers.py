from fastapi import APIRouter

from app.services.wb_client import get_search_results

routers = APIRouter(tags=["Search"])
@routers.get("/search")
def search(search: str):
    get_search_results(search)
    return {"message": f"Searching for {search}"}
