from click.testing import CliRunner
from insurance.interfaces.cli import cli
import sqlite3

def test_init_db_creates_tables(tmp_path):
    db_path = tmp_path / "test.db"
    print(db_path)
    runner = CliRunner()
    result = runner.invoke(cli, ["init-db", "--db", str(db_path)])
    assert result.exit_code == 0

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM insurance_policies")
    table = cursor.fetchone()
    assert table[0] == 3, "Table 'insurance_policies' should exist after init-db command."

    conn.close()