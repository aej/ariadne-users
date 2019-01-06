from typing import Union

from pydantic import EmailStr, BaseModel
from pydantic.dataclasses import dataclass


class User(BaseModel):
    email: EmailStr
    firstName: str
    lastName: str
    id: int = None


user_types = """
    type User {
        id: Int!
        email: String!
        firstName: String!
        lastName: String!
    }

    type CreateUserResponse {
        errors: [Error!]
        user: User
    }

    type Query {
        getUser(id: Int!): User
        listUsers: [User]!
    }

    type Mutation {
        createUser(email: String!, firstName: String!, lastName: String!): CreateUserResponse! 
    }
"""
