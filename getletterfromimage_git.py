import pytesseract
import psycopg2
import re
from PIL import Image
import os
# 画像ファイルを読み込む
#image = Image.open('/Users/mitsuiyuka/Documents/Documents - 三井由夏’s MacBook Air/Python/image.jpg')
#/Users/mitsuiyuka/Documents/Documents - 三井由夏’s MacBook Air/Python

# OCRを実行する
#text = pytesseract.image_to_string(image)

# OCRを実行する関数
def perform_ocr(image_path):
    # 画像ファイルを読み込む
    image = Image.open(image_path)

    # OCRを実行する
    text = pytesseract.image_to_string(image)

    return text

#整形
# Titleカラムに登録する文字列を抽出
title = re.findall(r"Soaring: Fantastic Flight", text, re.IGNORECASE)
if title:
    title = "soaring"
else:
    title = ""

# Contentカラムに登録する数字を抽出
match = re.search(r"(\d+)\s*min\.", text)
if match:
    content = match.group(1)
else:
    content = ""

print("Title:", title)
print("Content:", content)

# データベース接続の詳細設定
host = #  ホスト
dbname = #  スキーマ
user =  # ユーザー名
password = # パスワード

try:
    # PostgreSQLデータベースに接続
    conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password)
    cur = conn.cursor()

    # sql = "ALTER TABLE your_table_name ALTER COLUMN content TYPE VARCHAR(300)"
    # cur.execute(sql)
    
    # クエリを実行してデータを挿入
    sql = "INSERT INTO your_table_name (thread_id, Title, name, Content, delflg) VALUES (%s, %s, %s, %s, '0')"
    thread_id = '1'
    # title = 'ディズニーテスト'
    username ='ななし'
    # content = text
    cur.execute(sql, (thread_id, title, username, content))

    # 変更をコミット
    conn.commit()
    print('Insert successful')
    
    # 接続を閉じる
    cur.close()
    conn.close()

except psycopg2.Error as e:
    print('接続エラー:', e)
