import dash
from dash import dcc, html, Input, Output
import pandas as pd
import requests

# Загружаем данные
URL = "http://backend:8000/nocodb-data/"

def get_data():
    response = requests.get(URL)
    if response.status_code != 200:
        print(f"Ошибка запроса: {response.status_code}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame, если API недоступен
    
    try:
        data = response.json()
        records = data.get("records", [])  # Безопасно извлекаем записи
        return pd.DataFrame(records)
    except ValueError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return pd.DataFrame()

df = get_data()

if not df.empty:
    df = df.dropna(subset=["monitoring_id"])  # Убираем пустые записи
    df["monitoring_time"] = pd.to_datetime(df["monitoring_time"])
    df = df.sort_values("monitoring_time", ascending=True)

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Мониторинг виртуальных машин"),
    dcc.Graph(id="cpu-usage-graph"),
    dcc.Graph(id="memory-usage-graph"),
    dcc.Interval(
        id='interval-component',
        interval=5000,  # Обновление каждые 5 секунд
        n_intervals=0
    )
])

@app.callback(
    [
        Output("cpu-usage-graph", "figure"),
        Output("memory-usage-graph", "figure")
    ],
    Input("interval-component", "n_intervals")
)
def update_graphs(n):
    df = get_data()

    if df.empty:
        return {"data": [], "layout": {"title": "Нет данных"}}, {"data": [], "layout": {"title": "Нет данных"}}

    df = df.dropna(subset=["monitoring_id"])  # Убираем пустые записи
    df["monitoring_time"] = pd.to_datetime(df["monitoring_time"])
    df = df.sort_values("monitoring_time", ascending=True)
    
    cpu_fig = {
        "data": [{
            "x": df["monitoring_time"],
            "y": df["cpu_usage"],
            "type": "line",
            "name": "CPU Usage (%)"
        }],
        "layout": {"title": "Использование процессора"}
    }
    
    memory_fig = {
        "data": [{
            "x": df["monitoring_time"],
            "y": df["memory_usage"],
            "type": "line",
            "name": "Memory Usage (%)"
        }],
        "layout": {"title": "Использование памяти"}
    }
    
    return cpu_fig, memory_fig

if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")
