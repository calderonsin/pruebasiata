# Como correr el proyecto
1. python -m venv ./venv/
2. \venv\Scripts\activate
3. cd .\app\
4. pip install fastapi uvicorn fastapi SQLAlchemy pyscopg2
5. uvicorn main:app --reload --port 6969
