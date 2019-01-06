from ariadne import GraphQLMiddleware

from users import user_resolvers, user_types
from core import core_types

types = [core_types, user_types]

resolvers = [user_resolvers]

server = GraphQLMiddleware.make_simple_server(types, resolvers)
