# import_csv_to_postgres.py
import pandas as pd
from sqlalchemy import create_engine

# CSVファイルのパス
csv_file_path = '/home/akkunn/csv_import_project/import_csv/MN-.csv'  # 適切なパスに変更

# PostgreSQLのデータベース接続情報
db_url = 'postgresql://yuka:postgres@localhost/gasoline_price'

# エンジンの作成
engine = create_engine(db_url)

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)

# 日付フォーマットを変換
df['SurveyDate'] = pd.to_datetime(df['SurveyDate'], format='%Y/%m/%d')

# データフレームをPostgreSQLにインポート
df.to_sql('gasoline_price', engine, if_exists='replace', index=False)
