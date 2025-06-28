# 💾 Persistent GPT-4o Agent (LangGraph + Streamlit)

A minimal yet powerful conversational agent using **LangGraph**, **LangChain**, and **Streamlit**, built on top of GPT-4o.  
This chatbot supports:

✅ Persistent sessions using SQLite  
✅ Multi-session management with dynamic switching  
✅ Full support for tool and function messages  
✅ Clean Streamlit UI with sidebar-based session controls  

---

## 🧠 Features

- **Streamlit Interface**  
  Chat with the agent directly in the browser with a friendly interface.

- **Session Management**  
  Create and switch between multiple named sessions — all conversations are saved.

- **SQLite Database Integration**  
  Message and session history are stored persistently in a local SQLite file.

- **Supports Tool & Function Messages**  
  Structured messages like `ToolMessage` and `FunctionMessage` are stored and restored seamlessly.

- **LangGraph Agent Backend**  
  Built using LangGraph for flexible agent orchestration and memory management.

---

## 📁 Folder Structure
```
├── agent.py # LangGraph agent logic
├── main.py # Streamlit frontend
├── github_gpt4o_langchain.py # GPT-4o wrapper for GitHub inference endpoint
├── chat_messages.db # SQLite DB file (auto-created)
└── requirements.txt
```


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/persistent-gpt4o-agent.git
cd persistent-gpt4o-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a .env file:

```bash
OPENAI_API_KEY=your_api_key
```

### 4. Run the App

```bash
streamlit run main.py
```

### 🗂️ How it Works
- On first load, the app prompts you to either select an existing session or create a new one.
- Messages are saved in chat_messages.db under their respective session IDs.
- The LangGraph agent processes your input and returns AI responses.
- All message types (human, ai, system, function, tool) are stored with relevant metadata (tool_call_id, name).

### 🛠️ Future Additions
 -> Add real working tools (e.g., calculator, web search, weather)
 -> Export conversations
 -> Session tagging / summarization
 -> User authentication (optional)

### 📸 Preview
![image](https://github.com/user-attachments/assets/2c2e2231-3203-42f7-a608-5ecb88693bb6)

### 🧑‍💻 Author
Jayesh Suryawanshi
- 🧠 Python Developer | 💡 AI Tools Builder | 🌍 Data & Engineering Enthusiast
- 📫 [LinkedIn](https://www.linkedin.com/in/jayesh-suryawanshi-858bb21aa/)

### 📃 License
MIT License
