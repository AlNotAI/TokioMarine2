import pathlib

SQL_DIR = pathlib.Path(__file__).parent / "sql"

def load_sql(filename):
    """
    Load an SQL file from insurance/infrastructure/sql/<filename>.
    """
    path = SQL_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"SQL file not found: {path}")
    return path.read_text(encoding="utf-8")