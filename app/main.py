from fastapi import FastAPI

from app.advertisements.router import add_router as router_advertisements, category_router as category_router, pricing_router as pricing_router
app = FastAPI()


app.include_router(router_advertisements)
app.include_router(category_router)
app.include_router(pricing_router)


# class SAdvertisement(BaseModel):
#     description: str
#     date_from: date
#     date_to: date
#
#
# class AdvertisementsSearchArgs:
#     def __init__(
#             self,
#             description: str,
#             date_from: date,
#             date_to: date,
#             media_file: UploadFile = File(...),
#     ):
#         self.description = description
#         self.date_from = date_from
#         self.date_to = date_to
#         self.media_file = media_file
#
#         valid_image_types = ["image/jpeg", "image/png", "image/gif"]
#         if self.media_file.content_type not in valid_image_types:
#             raise HTTPException(status_code=400, detail="Invalid file type. Only image files are allowed.")
#
#
# @app.get("/advertisements/get")
# async def get_advertisements(search_args: AdvertisementsSearchArgs = Depends()):
#
#     return search_args
#
#
# @app.post("/advertisements/add")
# async def add_advertisement(
#         advertisement: SAdvertisement,
#         media_file: UploadFile = File(...)
#         ):
#
#     valid_image_types = ["image/jpeg", "image/png", "image/gif"]
#     if media_file.content_type not in valid_image_types:
#         raise HTTPException(status_code=400, detail="Invalid file type. Only image files are allowed.")
#
#     pass
#     return {
#         "description": advertisement.description,
#         "date_from": advertisement.date_from,
#         "date_to": advertisement.date_to,
#         "filename": media_file.filename
#     }
