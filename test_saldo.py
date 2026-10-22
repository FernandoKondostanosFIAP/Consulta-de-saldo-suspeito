import sqlite3
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

class TestSaldo(unittest.TestCase):
    def test_saldo_por_cliente(self):
        con = sqlite3.connect(':memory:')
        try:
            con.executescript((ROOT/'dados.sql').read_text(encoding='utf8'))
            sql = (ROOT/'consulta_saldo.sql').read_text(encoding='utf8')
            rows = {nome: saldo for nome, saldo in con.execute(sql).fetchall()}
            self.assertEqual(rows, {'Ana': 750.0, 'Bruno': -80.0, 'Carla': 60.0})
        finally:
            con.close()

if __name__ == '__main__':
    unittest.main()
