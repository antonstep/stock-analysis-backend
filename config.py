import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('postgres://stock_analysis_backend_user:87UcUha5aNxtWZPQ9fLtPmzE2HgRUVnc@dpg-cpcblovjbltc73ac7ngg-a/stock_analysis_backend')