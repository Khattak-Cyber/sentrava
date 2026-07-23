from pydantic import BaseModel

class CompanyCreate(BaseModel):
    name: str
    email: str
    industry: str

class CompanyResponse(CompanyCreate):
    id: int

    class Config:
        from_attributes = True