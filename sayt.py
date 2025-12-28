import os
from flask import Flask, render_template
from dotenv import load_dotenv
from supabase import create_client

# Подгружаем секретные ключи из .env
load_dotenv()

app = Flask(__name__)

# Инициализируем связь с базой Supabase
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.route('/')
def home():
    try:
        # Получаем товары из таблицы 'products'
        response = supabase.table("products").select("*").execute()
        items = response.data
    except Exception as e:
        print(f"Ошибка получения данных: {e}")
        items = []
    
    return render_template('index.html', clothes=items)

if __name__ == "__main__":
    app.run(debug=True)