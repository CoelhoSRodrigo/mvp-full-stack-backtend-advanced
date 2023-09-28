from pydantic import BaseModel


class ErrorSchema(BaseModel):
    """Schema que representa como um erro será retornado pela API"""

    error_msg: str
