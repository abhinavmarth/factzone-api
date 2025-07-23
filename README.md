# factzone-api
---

### ✅ COMPLETE `README.md` CONTENT FOR YOUR DOCKERIZED FLASK FACT API

```markdown
# 🧠 FactZone - Dockerized Flask REST API

**FactZone** is a lightweight, Dockerized Flask API that serves random programming facts through a clean RESTful interface. Designed for simplicity, quick deployment, and beginner-level contribution, it’s a great starting point for containerized backend development.

---

## 📌 Project Highlights

- ✅ Built with **Flask** in **Python 3.10+**
- 🐳 Fully **Dockerized** — portable, consistent, and easy to run anywhere
- 🔁 Supports **GET** requests for different fact categories
- 💡 Clean project structure — ideal for beginners and educational use
- 📦 Minimal dependencies

---

## 🧱 Tech Stack

| Layer        | Tech            |
|--------------|-----------------|
| Language     | Python 3.10     |
| Framework    | Flask           |
| Container    | Docker          |
| Package Mgmt | `pip`, `requirements.txt` |

---

## 📂 Project Structure

```

factzone-api/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Instructions to build Docker image
└── README.md           # You're reading this!

````

---

## 📥 Installation & Local Setup

### ✅ Clone the repo

```bash
git clone https://github.com/abhinavmarth/factzone-api.git
cd factzone-api
````

### ✅ Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows
```

### ✅ Install dependencies

```bash
pip install -r requirements.txt
```

### ✅ Run the app

```bash
python app.py
```

Visit `http://localhost:5000/fact/programming` in your browser or use Postman.

---

## 🐳 Run with Docker

### ✅ Build the image

```bash
docker build -t factzone .
```

### ✅ Run the container

```bash
docker run -p 5000:5000 factzone
```

Visit: [http://localhost:5000/fact/programming](http://localhost:5000/fact/programming)

---

## 🔗 API Endpoint

| Method | URL                | Description           |
| ------ | ------------------ | --------------------- |
| GET    | `/fact/<category>` | Returns a random fact |

### Example:

```
GET /fact/programming
```

### Sample Output:

```json
{
  "topic": "programming",
  "fact": "Python was named after the British comedy group Monty Python."
}
```

---

## 📌 Use in Your Resume

> **Designed and deployed a Flask REST API (`FactZone`) containerized using Docker. The application serves dynamic fact-based content via clean REST endpoints. Built using Python, Flask, and Docker. Demonstrated skills in containerization, REST API development, and clean code architecture.**

---

## 🚀 Potential Enhancements

* 🔄 Add support for custom user-submitted facts (POST method)
* 🧠 Use a database (SQLite/PostgreSQL) for persistent storage
* 📘 Add Swagger/OpenAPI documentation
* 🌍 Deploy to Render, Railway, EC2, or Vercel

---

## 🙌 Author

Made with ❤️ by [Abhinav Martha](https://github.com/abhinavmarth)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

```

---

## ✅ Want Add-Ons?

Let me know if you want:
- A `.dockerignore` file  
- A `requirements.txt` example  
- CI/CD with GitHub Actions  
- Deployment instructions (Render, Railway, AWS EC2)  

I'm happy to help you scale this into a real portfolio project!
```
