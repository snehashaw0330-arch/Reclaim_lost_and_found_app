import sqlite3
from typing import Optional, List, Dict

DB_PATH = "metadata.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id TEXT PRIMARY KEY,
            image_path TEXT NOT NULL,
            contact_number TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def insert_item(item_id: str, image_path: str, contact_number: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO items (id, image_path, contact_number) VALUES (?, ?, ?)",
        (item_id, image_path, contact_number)
    )

    conn.commit()
    conn.close()


def get_item(item_id: str) -> Optional[Dict]:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, image_path, contact_number FROM items WHERE id = ?",
        (item_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "image_path": row[1],
        "contact_number": row[2]
    }


def get_items(item_ids: List[str]) -> List[Dict]:
    if not item_ids:
        return []

    placeholders = ",".join("?" for _ in item_ids)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"SELECT id, image_path, contact_number FROM items WHERE id IN ({placeholders})",
        item_ids
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "image_path": row[1],
            "contact_number": row[2]
        }
        for row in rows
    ]