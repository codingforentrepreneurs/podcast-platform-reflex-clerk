from pydantic import BaseModel, field_validator


class ContactMessageCreateSchema(BaseModel):
    name: str
    message: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, val):
        if "justing" in str(val).lower():
            raise ValueError("Name cannot contain 'Justin'" )
        return val
