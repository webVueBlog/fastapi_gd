# 设置项（密钥、数据库）

# config.py

SECRET_KEY = "123456"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# MySQL 连接字符串：请替换用户名、密码、主机、库名
DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/fastapi_demo?charset=utf8mb4"

