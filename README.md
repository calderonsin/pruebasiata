# Como correr el proyecto
python -m venv ./venv/
\venv\Scripts\activate
cd .\app\
pip install fastapi uvicorn fastapi SQLAlchemy pyscopg2
uvicorn main:app --reload --port 6969
