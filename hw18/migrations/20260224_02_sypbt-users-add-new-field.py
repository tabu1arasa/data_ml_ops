"""
users: add new field
"""

from yoyo import step

__depends__ = {'20260224_01_p1bxR-users-create-table'}

steps = [
    step(
        # migration
        """
            alter table users add nickname varchar(100) null;
        """,
        # rollback
        """
            alter table users drop column nickname;
        """
    )
]
