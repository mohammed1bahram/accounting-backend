# Accountant's Blueprint API – Backend (FastAPI)

## What is this?
A starter backend app using FastAPI and SQLAlchemy, ready to connect to your Supabase (PostgreSQL) accounting database.

---

## 1. Prepare Your Credentials

- Get your Supabase database connection info:
    - Host
    - Database
    - User (usually "postgres")
    - Password
    - Port (usually 5432)

---

## 2. How to Run on [Replit](https://replit.com/) (No coding needed)

1. **Go to [https://replit.com/~](https://replit.com/~) and create a free account.**
2. **Click "Create Repl" > Choose "Python" template.**
3. **Upload all the files from this project.**
4. **Set your database credentials:**
    - In Replit, click the "Secrets" (lock icon) in the left sidebar.
    - Add:
        - `DB_USER` = your Supabase user
        - `DB_PASS` = your Supabase password
        - `DB_HOST` = your Supabase host (like `db.xxxx.supabase.co`)
        - `DB_PORT` = 5432
        - `DB_NAME` = postgres
5. **In the Replit Shell (bottom panel), run:**
    ```
    pip install -r requirements.txt
    ```
6. **Start the server:**
    ```
    uvicorn main:app --reload --host=0.0.0.0 --port=8000
    ```
7. **You will see your API running!**
    - Visit the API docs: `https://[your-repl-username].[your-repl-name].repl.co/docs`

---

## 3. How to Run Locally (on your own computer)

1. Install Python 3.11+ from [python.org](https://python.org)
2. Open a terminal/command prompt.
3. Download all these files to a folder.
4. Run:
    ```
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```
5. API will be at: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 4. How to Deploy to the Cloud (Render, DigitalOcean, etc.)

- You can use the Dockerfile for deployment.
- On most platforms, just connect your repo or upload the code, and add your database credentials as environment variables.

---

## 5. Next Steps

- Add more endpoints (items, invoices, etc.) as needed!
- Connect a frontend (React) for dashboards and forms.
- Multi-language support can be enabled using FastAPI middleware and frontend i18n.

---

**Need help?**  
Ask Copilot or any developer to help you extend this starter!