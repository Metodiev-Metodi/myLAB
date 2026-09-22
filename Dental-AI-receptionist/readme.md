# 🦷 Dental AI Receptionist

An AI-powered virtual dental receptionist built for **Boyanova Dent**, combining conversational AI, RAG, PostgreSQL/pgvector, n8n workflow automation and Google Calendar.

The project is designed to handle common dental receptionist tasks through a natural-language chat interface — answering general dental questions, checking appointment availability and assisting with appointment management.

> **Project type:** AI Automation / RAG / Conversational AI / Workflow Automation

---

## 🚀 Project Overview

The Dental AI Receptionist goes beyond a traditional chatbot.

It combines:

- 🤖 AI Agent orchestration
- 📚 Retrieval-Augmented Generation (RAG)
- 🧠 Semantic search with embeddings
- 🗄️ PostgreSQL + pgvector
- 📅 Google Calendar integration
- 🕒 Natural-language date and time handling
- 💬 Conversation memory
- 🔄 n8n workflow automation
- 🌐 Web chat integration

The assistant is designed to act as a digital first-line receptionist for a dental practice while keeping the knowledge used for dental information answers inside a controlled knowledge base.

---

## 🏗️ Architecture

~~~text
                    ┌──────────────────────┐
                    │        Patient       │
                    │      / Website       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Chat Interface  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     n8n Webhook      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       AI Agent       │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      ┌──────────────┐  ┌──────────────┐  ┌────────────────┐
      │   Dental RAG │  │ Date & Time  │  │ Google Calendar│
      │  Knowledge   │  │  Calculator  │  │     Tools      │
      └──────┬───────┘  └──────────────┘  └───────┬────────┘
             │                                     │
             ▼                                     ▼
      ┌──────────────┐                    ┌────────────────┐
      │ PostgreSQL   │                    │ Availability   │
      │  + pgvector  │                    │ Booking        │
      └──────────────┘                    │ Rescheduling   │
                                          │ Cancellation   │
                                          └────────────────┘
~~~

---

## 🧠 RAG Knowledge Base

The assistant uses **Retrieval-Augmented Generation** instead of relying only on the language model's general knowledge.

The document pipeline is:

~~~text
Dental Documents
       ↓
Read / Extract Text
       ↓
JavaScript Chunking
       ↓
Document Metadata
       ↓
Embeddings
       ↓
PostgreSQL + pgvector
       ↓
Semantic Search
       ↓
AI Agent
       ↓
Response
~~~

Documents are divided into smaller overlapping chunks and stored together with metadata describing their source.

### Vector database

Main table:

~~~text
public.dental_knowledge
~~~

Typical structure:

~~~text
dental_knowledge
├── id
├── content
├── embedding
└── metadata
~~~

Embeddings are stored as vectors and searched using **pgvector**.

Current embedding configuration:

~~~text
text-embedding-3-small
vector(1536)
~~~

---

## 🔎 Semantic Search

When a user asks a dental-related question:

1. The question is sent to the AI Agent.
2. The agent can query the dental knowledge base.
3. PostgreSQL performs vector similarity search.
4. Relevant document chunks are returned.
5. The AI Agent uses the retrieved context to generate the response.

This provides a controlled knowledge-retrieval layer between the user and the language model.

---

## 📅 Appointment Management

The AI Agent is integrated with **Google Calendar**.

The workflow can work with:

- Appointment availability
- Date-specific availability
- Requested time slots
- Creating appointments
- Retrieving existing events
- Cancelling appointments
- Rescheduling appointments

Before creating an appointment, the assistant is designed to collect the required patient information, including:

- Full name
- Phone number
- Reason for the visit
- Requested date and time

The information can then be used to create a structured calendar event.

---

## 🕒 Date & Time Handling

Date calculations are handled by a dedicated **Date Calculator** rather than asking the language model to manually calculate dates.

The system is configured around:

~~~text
Timezone: Europe/Sofia
Working days: Monday – Friday
Working hours: 09:00 – 17:00
Slot duration: 30 minutes
~~~

It supports natural-language expressions such as:

~~~text
today
tomorrow
next Monday
Friday
утре
следващия понеделник
петък
12 септември
12.09.2026
~~~

The calculator produces standardized ISO 8601 timestamps, for example:

~~~text
2026-09-07T09:00:00+03:00
2026-09-07T17:00:00+03:00
~~~

This reduces ambiguity when working with calendar events and natural-language dates.

---

## 💬 Conversation Memory

Conversation memory allows the assistant to maintain context between messages.

Example:

~~~text
User: Има ли свободен час утре?

AI: Да, има свободни часове.

User: А в 13:00?

AI: Да, 13:00 е свободен.

User: Запази го.

AI: Разбира се. Моля, кажете име и телефонен номер.
~~~

The assistant can use the previous conversation context to understand phrases such as:

- "този час"
- "запази го"
- "премести го"
- "утре"

---

## 🌐 Website Integration

The AI receptionist can be exposed through a website chat interface.

The web application communicates with the n8n webhook using a simple JSON payload:

~~~json
{
  "chatInput": "Има ли свободен час утре?",
  "sessionId": "unique-session-id"
}
~~~

The n8n workflow processes the request and returns the assistant response.

Expected response format:

~~~json
{
  "output": "Да, има свободни часове..."
}
~~~

This keeps the website frontend relatively independent from the AI workflow.

---

## 🔐 Security & Privacy

No production credentials, API keys, passwords or private patient information should be stored in this repository.

The repository contains:

- Workflow configuration
- Database examples / schemas
- Demonstration assets
- Screenshots
- Documentation

Credentials for external services such as:

- LLM providers
- PostgreSQL
- Google Calendar

must be configured separately inside the local n8n environment.

> **Important:** Patient information and real appointment data should not be committed to GitHub.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **n8n** | Workflow automation and AI orchestration |
| **AI Agent** | Conversational decision making |
| **PostgreSQL** | Database and vector storage |
| **pgvector** | Vector similarity search |
| **OpenAI Embeddings** | Document embeddings |
| **JavaScript** | Date processing and workflow logic |
| **Google Calendar** | Appointment management |
| **RAG** | Knowledge retrieval |
| **PDF documents** | Knowledge-base sources |
| **Webhook API** | Website ↔ n8n communication |

---

## 📂 Repository Structure

~~~text
Dental-AI-receptionist/
│
├── database/
│   ├── Schema.png
│   └── rag-sources.png
│
├── demo/
│   ├── n8n.mp4
│   └── n8n.gif
│
├── screenshots/
│   ├── Create_event.png
│   ├── RAG.png
│   ├── RAG_usage.png
│   └── RAG_.png
│
├── workflow/
│   └── Dental AI receptionist.json
│
└── readme.md
~~~

---

## 🎥 Demo

### n8n AI Receptionist

[▶️ Watch the Dental AI Receptionist Demo](demo/n8n.mp4)

![Dental AI Receptionist Demo](demo/n8n.gif)

---

## 📸 Screenshots

### Appointment Workflow

![Appointment Workflow](screenshots/Create_event.png)

### RAG Retrieval

![RAG Retrieval](screenshots/RAG.png)

![RAG Usage](screenshots/RAG_usage.png)

![RAG Workflow](screenshots/RAG_.png)

### PostgreSQL / pgvector

![PostgreSQL Schema](database/Schema.png)

### RAG Sources

![RAG Sources](database/rag-sources.png)

---

## ⚙️ Setup

### 1. Install n8n

Run n8n locally or connect to an existing n8n instance.

### 2. Configure PostgreSQL

Create a PostgreSQL database and enable the **pgvector** extension.

### 3. Import the workflow

Import:

~~~text
workflow/Dental AI receptionist.json
~~~

into n8n.

### 4. Configure credentials

Configure the required credentials for:

- LLM / embeddings
- PostgreSQL
- Google Calendar

### 5. Configure the knowledge base

Add the required dental documents to the ingestion workflow and generate the embeddings.

### 6. Configure the calendar

Connect the Google Calendar account used for appointment management.

### 7. Connect the website

Configure the website to send:

~~~json
{
  "chatInput": "user message",
  "sessionId": "session-id"
}
~~~

to the n8n webhook.

---

## 🔄 Example Workflow

~~~text
User Message
     ↓
Website Chat
     ↓
n8n Webhook
     ↓
AI Agent
     │
     ├── Dental RAG
     │      └── PostgreSQL + pgvector
     │
     ├── Date Calculator
     │
     ├── Conversation Memory
     │
     └── Google Calendar
             ↓
        Appointment Tools
             ↓
        AI Response
             ↓
        Website Chat
~~~

---

## 🚧 Current Development Focus

The project is being developed as a practical AI receptionist rather than a static chatbot.

Current areas include:

- Reliable natural-language date handling
- Appointment availability checks
- Calendar booking flows
- Rescheduling and cancellation
- RAG retrieval quality
- Conversation context
- Website integration
- Production deployment
- Error handling and validation

---

## 🔮 Future Improvements

Potential next steps include:

- Appointment confirmation messages
- Automatic reminders
- Improved conflict handling
- Better appointment validation
- Patient database integration
- Source references in RAG answers
- Improved multilingual support
- Voice receptionist integration
- Monitoring and logging
- Production-grade authentication
- Improved privacy controls
- Analytics for receptionist interactions

---

## 🎯 Project Goal

The goal of this project is to demonstrate how modern AI components can be combined into a practical business automation solution.

Instead of building only a chatbot, the project connects:

**LLM + RAG + Vector Database + Workflow Automation + APIs + Calendar**

into a system capable of handling real-world receptionist workflows.

---

## 👨‍💻 About

Built as a practical AI automation project using **n8n, PostgreSQL/pgvector, RAG and conversational AI**.

The project is part of a broader portfolio focused on:

- AI automation
- Data & analytics
- Workflow automation
- RAG systems
- Business process automation
- IT infrastructure
