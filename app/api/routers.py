from io import BytesIO

from fastapi import APIRouter
from starlette.responses import StreamingResponse

from app.services.wb_client import get_search_results, from_dict_get_excel

routers = APIRouter(tags=["Search"])
@routers.get("/search")
def search(search: str, min_rating : float = None, max_price : int = None):
    total_info = get_search_results(search)
    xlsx_bytes = from_dict_get_excel(total_info,min_rating,max_price)

    return StreamingResponse(
        BytesIO(xlsx_bytes),
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": 'attachment; filename="products.xlsx"'},
    )


