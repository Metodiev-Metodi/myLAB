# IT & Data Analytics Portfolio

## 👨‍💻 About Me

IT and Data professional with **10+ years of experience in IT Operations** and **1.5+ years of hands-on experience in Data Analytics and BI**.

My recent experience includes working with **SQL, data validation, data analysis, data modeling, Dremio and Power BI**, with a focus on transforming business requirements into reliable analytical datasets and dashboards.

I have worked closely with business stakeholders to understand requirements, validate data, prepare datasets and deliver meaningful reporting and visualizations.

My previous IT Operations experience provides a strong technical foundation in troubleshooting, systems, access management, security, compliance and stakeholder communication.

## 🛠️ Core Skills

### Data & BI

- SQL
- Data Analysis
- Data Validation
- Data Modeling
- Power BI
- Dremio
- ETL / Data Preparation
- Dashboard Development

### IT & Infrastructure

- IT Operations
- Troubleshooting
- Active Directory
- Access Management
- Software Deployment
- Security & Compliance

### Automation

- n8n
- AI Agents
- RAG
- Vector Databases
- PostgreSQL / pgvector
- Embeddings
- API Integrations
- Webhooks

---

# Projects

## 1. AI-Powered Dental Receptionist

An AI-powered dental reception assistant built with n8n, RAG, PostgreSQL/pgvector, embeddings, JavaScript and Google Calendar.

The project demonstrates how an AI agent can combine a document-based knowledge base with external tools to answer dental information questions and manage real-world appointment workflows.

Key Features
- RAG-based dental knowledge retrieval
- PDF document ingestion and chunking
- Semantic search using PostgreSQL + pgvector
- AI Agent orchestration with n8n
- Google Calendar availability checking
- Appointment creation, cancellation and rescheduling
- Natural-language date and time handling
- Conversation memory
- Patient name and phone collection during booking
Architecture
User
 ↓
n8n AI Agent
 ├── Dental Knowledge Base
 │      ↓
 │   Embeddings
 │      ↓
 │   PostgreSQL + pgvector
 │
 ├── Date Calculator
 │
 ├── Conversation Memory
 │
 └── Google Calendar
        ├── Availability
        ├── Create Event
        ├── Get Appointments
        ├── Cancel
        └── Reschedule
Technologies

n8n · AI Agent · RAG · PostgreSQL · pgvector · Embeddings · JavaScript · Google Calendar

Project Repository

👉 [View the full Dental AI Receptionist project](Dental-AI-receptionist/)
![Dental AI Receptionist](Dental-AI-receptionist/screenshots/Create_event.png)
The project repository contains the n8n workflow, database screenshots, RAG retrieval examples and project documentation.


## 2. AI-Powered Sales Analytics Dashboard

An automated data-to-dashboard pipeline built with **n8n, Azure SQL, SQL, AI and Chart.js**.

The workflow extracts analytical data from Azure SQL, processes and validates the datasets, uses AI to generate a dashboard specification, and generates an executive HTML dashboard.

### Architecture

```text
Azure SQL
    ↓
SQL Queries
    ↓
n8n
    ↓
Data Processing & Validation
    ↓
AI Dashboard Specification
    ↓
AI HTML Generation
    ↓
Chart.js Dashboard
    ↓
Webhook
```
![w](AI-sales-dashboard/screenshots/n8n_AI_architecture.png)
![Sales and Orders Executive Dashboard](AI-sales-dashboard/screenshots/Dashboard_Sales.png)

## 3. IT Analytics Dashboard

An analytics project focused on IT operational data and business-oriented reporting.

### Technologies

- SQL
- Power BI
- Data Analytics
- Data Modeling
- BI Dashboards

### Key areas

- IT operational metrics
- Data validation
- KPI analysis
- Dashboard development
- Business insights

### Dashboard Preview

![Overview Dashboard](IT-Support-Analytics//screenshots/Dashboard.png)

---
