# import_csv_to_postgres.py
import pandas as pd
from sqlalchemy import create_engine

# CSVファイルのパス
csv_file_path = '/home/akkunn/MNEX_SQL_TEST/import_csv/user.csv'  # 適切なパスに変更

# PostgreSQLのデータベース接続情報
db_url = 'postgresql+psycopg2://postgres:postgres@localhost/mnex'

# エンジンの作成
engine = create_engine(db_url)

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)


# データフレームをPostgreSQLにインポート
df.to_sql('users', engine, if_exists='append', index=False)
