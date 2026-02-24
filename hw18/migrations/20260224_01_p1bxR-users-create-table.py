"""
users: create table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        # migration
        """
            create table users (
                user_id integer primary key generated always as identity,
                username varchar(50) not null,
                birthdate date not null,
                email varchar(100) unique not null
            );
        """,
        # rollback
        """
            drop table users;
        """
    )
]
