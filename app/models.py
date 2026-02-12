from pydantic import BaseModel, Field

class Procedure(BaseModel):
    id: int = Field(..., title="The ID of the procedure")
    name: str = Field(..., title="The name of the procedure")
    description: str = Field(..., title="A brief description of the procedure")
    created_at: str = Field(..., title="Creation timestamp of the procedure")
    updated_at: str = Field(..., title="Last updated timestamp of the procedure")

class ProcedureResponse(BaseModel):
    procedure: Procedure

class ProcedureListResponse(BaseModel):
    procedures: list[Procedure]