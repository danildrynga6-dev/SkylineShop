import os
from flask import Flask, render_template
from supabase import create_client

app = Flask(__name__, template_folder='templates')

# Подключение к базе данных
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

# Проверка, что ключи вообще загрузились
if not url or not key:
    print("ОШИБКА: Ключи Supabase не найдены в настройках Vercel!")

supabase = create_client(url, key)

@app.route('/')
def index():
    try:
        # Пытаемся забрать данные из таблицы 'shoes'
        response = supabase.table('shoes').select("*").execute()
        shoes_list = response.data
        return render_template('index.html', shoes=shoes_list)
    except Exception as e:
        # Если таблица называется иначе, сайт покажет саму ошибку, а не просто 500
        return f"Ошибка подключения к базе: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
