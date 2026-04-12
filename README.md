# 🚀 KeyVaultX – API Key Management System

A professional backend project built using **FastAPI** that allows secure generation, storage, retrieval, and deletion of API keys using a structured database system.

---

## 🔥 Key Features

- 🔐 Generate secure API keys
- 💾 Store API keys in SQLite database
- 📥 Retrieve all stored API keys
- 🗑️ Delete API keys using unique ID
- ⚡ Fast and high-performance API using FastAPI
- 📊 Interactive API testing via Swagger UI

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** SQLite
- **ORM:** SQLAlchemy
- **Server:** Uvicorn
- **API Testing:** Swagger UI (/docs)

---

## 📌 API Endpoints

### 1️⃣ Generate API Key
POST /generate-key

✔ Generates a secure API key  
✔ Stores it in database  

---

### 2️⃣ Get All API Keys
GET /get-keys

✔ Fetches all stored API keys  
✔ Returns list of keys with ID  

---

### 3️⃣ Delete API Key
DELETE /delete-key/{id}

✔ Deletes API key using ID  
✔ Returns success or not found message  

---

## ▶️ Run Locally

```bash
uvicorn main:app --reload
Open in browser:

http://127.0.0.1:8000/docs
