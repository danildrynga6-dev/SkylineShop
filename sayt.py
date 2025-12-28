import os
from flask import Flask, render_template
from supabase import create_client

app = Flask(__name__, template_folder='templates')

# --- ВОТ СЮДА ВСТАВЛЯЕМ ЭТОТ БЛОК ---
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)
# ------------------------------------

@app.route('/')
def index():
    # Запрос данных из таблицы 'shoes' (убедись, что таблица так называется)
    response = supabase.table('shoes').select("*").execute()
    shoes_list = response.data
    return render_template('index.html', shoes=shoes_list)

if __name__ == '__main__':
    app.run(debug=True)


