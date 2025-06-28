# 💾 Persistent Github GPT-4o Agent (LangGraph + Streamlit) 

A powerful, privacy-conscious AI assistant powered by GitHub-hosted GPT-4o.  
Designed with developers in mind, this agent offers persistent session memory, secure token authentication, and extendability for real-world applications.

---

## 🔐 Authentication via GitHub Token

- Secure login via GitHub token (user-provided).
- Each token is **SHA-256 hashed** to create a private identifier (`user_hash`) used to:
  - Track user sessions
  - Prevent token storage
  - Isolate chat histories across users

> 💡 You can generate a GitHub token from:  
> [https://github.com/settings/tokens](https://github.com/settings/tokens)

---

## 💾 Persistent Memory via SQLite

- All chat messages are stored in a local database (`chat_messages.db`).
- Each user can create and manage **multiple chat sessions**.
- All message types (`human`, `AI`, `function`, `tool`, etc.) are serialized and deserialized correctly.

---

## 🧠 LangGraph Architecture

- Built using LangGraph's `StateGraph` for controlled message flow.
- Node function (`process`) invokes the model and updates memory.
- Designed to be extensible for:
  - Tool calling
  - Function execution
  - Retrieval-augmented generation

---

## 🧠 Highlights

| Feature                  | Details |
|--------------------------|---------|
| 🛡️ Token Hashing         | Prevents token leaks and supports session-based user isolation |
| 🗃️ Session Management    | Named session support with persistent conversations |
| 🧠 GPT-4o Integration     | Uses GitHub's hosted inference endpoint (`https://models.github.ai/inference`) |
| 🔄 Tool & Function Ready | Agent already supports future extensions for tool-calling and more |
| ❌ Invalid Token Check   | Validates GitHub token via trial request before login |
| 🔄 Logout Flow           | Secure reset and return to auth gate |

---
## 📂 Project Structure

```bash
├── main.py # Streamlit frontend with authentication and UI
├── agent.py # LangGraph logic and GPT-4o invocation flow
├── github_wrapper.py # Custom wrapper for GitHub-hosted GPT-4o API
├── chat_messages.db # SQLite database for chat/session persistence
├── requirements.txt # Python dependencies
└── README.md # Project overview and usage
```
---
## ⚙️ How to Use


### 1. Clone the repo:

```bash
git clone https://github.com/your-username/GitHub-GPT4o-Agent.git
cd GitHub-GPT4o-Agent
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run it:

```bash
streamlit run main.py
```

### 4. Provide your GitHub GPT-4o token at login
---
### 🔒 Security First
- GitHub tokens are not stored.
- All session control is hash-based and local.
- SQLite stores only messages, not secrets.
---
### 🧰 Tech Stack
- LangGraph & LangChain
- Streamlit
- SQLite (for state persistence)
- GitHub GPT-4o Inference API
---
### 📸 Previews
![image](https://github.com/user-attachments/assets/8021895f-de59-42a2-8c10-baef00491792)
---
### 🧑‍💻 Author
Jayesh Suryawanshi
- 🧠 Python Developer | 💡 AI Tools Builder | 🌍 Data & Engineering Enthusiast
- 📫 [LinkedIn](https://www.linkedin.com/in/jayesh-suryawanshi-858bb21aa/)
---
### 📃 License
MIT License
