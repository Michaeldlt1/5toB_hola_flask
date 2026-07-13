import os
from typing import Dict, List, Optional

import psycopg2
from psycopg2.extras import RealDictCursor


class DatabaseUserService:
    def __init__(self, fallback_users: Optional[List[Dict[str, str]]] = None):
        self.fallback_users = fallback_users or []
        self.db_available = False
        self._connect()

    def _connect(self):
        host = os.getenv("POSTGRES_HOST", "postgres")
        port = os.getenv("POSTGRES_PORT", "5432")
        dbname = os.getenv("POSTGRES_DB", "appdb")
        user = os.getenv("POSTGRES_USER", "appuser")
        password = os.getenv("POSTGRES_PASSWORD", "apppassword")

        try:
            self.conn = psycopg2.connect(
                host=host,
                port=port,
                dbname=dbname,
                user=user,
                password=password,
            )
            self.conn.autocommit = True
            self._init_schema()
            self.db_available = True
        except Exception:
            self.conn = None
            self.db_available = False

    def _init_schema(self):
        if not self.conn:
            return
        with self.conn.cursor() as cur:
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
                """
            )

    def create_user(self, name: str, email: str, password: str) -> Dict[str, str]:
        if self.db_available and self.conn:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute(
                    "INSERT INTO users (name, email, password) VALUES (%s, %s, %s) RETURNING id, name, email, password",
                    (name, email, password),
                )
                row = cur.fetchone()
                return dict(row)

        user = {"name": name, "email": email, "password": password}
        self.fallback_users.append(user)
        return user

    def list_users(self) -> List[Dict[str, str]]:
        if self.db_available and self.conn:
            with self.conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT name, email, password FROM users ORDER BY id")
                rows = cur.fetchall()
                return [dict(row) for row in rows]
        return self.fallback_users
