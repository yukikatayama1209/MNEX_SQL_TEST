from fastapi import FastAPI, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import DataTable

import plotly.graph_objects as go
from plotly.subplots import make_subplots


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# SQLAlchemyセッションの依存性注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# データを取得してPlotlyのFigureオブジェクトを返す関数
def get_plot_data(db: Session):
    data = db.query(DataTable).all()
    
    # デバッグ：取得したデータを確認する
    print(data)
    
    # グラフの作成（ここでは例として折れ線グラフを作成）
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[row.SurveyDate for row in data],
                             y=[row.Regular_Hokkaido for row in data],
                             mode='lines',
                             name='Regular Hokkaido'))
    fig.update_layout(title='Regular Hokkaido Prices Over Time')
    
    return fig

# データを取得してテンプレートに表示するエンドポイント
@app.get("/", response_class=HTMLResponse)
async def read_data(request: Request, db: Session = Depends(get_db)):
    data = db.query(DataTable).all()
    return templates.TemplateResponse("index2.html", {"request": request, "data": data})

# グラフを表示するエンドポイント
@app.get("/plot", response_class=HTMLResponse)
async def plot_data(request: Request, db: Session = Depends(get_db)):
    fig = get_plot_data(db)
    plot_div = fig.to_html(full_html=False, default_height=500, default_width=700)
    return templates.TemplateResponse("plot.html", {"request": request, "plot_div": plot_div})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
