import typing

import strawberry


if typing.TYPE_CHECKING:
    import tests.schema.test_lazy_types

    from .type_b import TypeB


@strawberry.type
class TypeA:
    list_of_b: typing.Optional[
        typing.List[strawberry.LazyType["TypeB", "tests.schema.test_lazy_types.type_b"]]
    ] = None

    @strawberry.field()
    def type_b(self) -> strawberry.LazyType["TypeB", ".type_b"]:  # noqa
        from .type_b import TypeB

        return TypeB()
