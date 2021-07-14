from fastapi_crudrouter import OrmarCRUDRouter

from . import models, schemas

category_router = OrmarCRUDRouter(
        schema=models.Category,
        create_schema=schemas.CategoryBase
)
post_router = OrmarCRUDRouter(
        schema=models.Post,
        create_schema=schemas.PostBase
)
comment_router = OrmarCRUDRouter(
        schema=models.Comment,
        create_schema=schemas.CommentBase
)
