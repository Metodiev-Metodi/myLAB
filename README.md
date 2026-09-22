# IT, Data & AI Portfolio

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
- PostgreSQL
- API Integrations
- Webhooks

---

# Projects

## 1. 🦷 AI-Powered Dental Receptionist - 🌐 **Live Website:** [Boyanova Dent](https://boyanovadent.com/)

An AI-powered dental reception assistant built for **Boyanova Dent**, combining **n8n, AI agents, RAG, PostgreSQL/pgvector, embeddings, Google Calendar and a Next.js web application**.

The project demonstrates how an AI agent can combine structured knowledge, clinic-specific policies and external tools to answer questions and manage real appointment workflows.

### Key Features

- Two RAG knowledge layers
- General dental knowledge retrieval
- **Dental_services_policy** for clinic-specific services and policies
- PDF document ingestion and chunking
- Semantic search using PostgreSQL + pgvector
- AI Agent orchestration with n8n
- Google Calendar availability checking
- Appointment creation, cancellation and rescheduling
- Natural-language date and time handling
- Conversation memory
- Patient information collection during booking
- Automated dental news section
- Next.js / React frontend
- Cloudflare Tunnel for webhook exposure
- Vercel deployment

### RAG Architecture

```text
                         User Question
                              │
                              ▼
                          AI Agent
                         /        \
                        /          \
                       ▼            ▼
           General Dental RAG   Dental_services_policy
                   │                    │
                   ▼                    ▼
            General dental       Clinic-specific
               knowledge        services & policies
                       \          /
                        \        /
                         ▼      ▼
                       AI Response
```

### Appointment Architecture

```text
User
  │
  ▼
Next.js Website
  │
  ▼
n8n Webhook
  │
  ▼
AI Agent
  │
  ├── General Dental RAG
  ├── Dental_services_policy
  ├── Date & Time Calculator
  ├── Conversation Memory
  │
  └── Google Calendar
          ├── Check Availability
          ├── Create Event
          ├── Get Appointments
          ├── Cancel Appointment
          └── Reschedule Appointment
```

### Automated Dental News

A separate n8n workflow collects and processes dental-related news for the website.

```text
News Sources
     ↓
n8n Workflow
     ↓
Content Extraction
     ↓
Dental Topic Filtering
     ↓
Article Processing
     ↓
Website News Section
```

### Technologies

**n8n · AI Agent · RAG · PostgreSQL · pgvector · OpenAI Embeddings · JavaScript · Google Calendar · Next.js · React · Vercel · Cloudflare Tunnel**

👉 **[View the full Dental AI Receptionist project](Dental-AI-receptionist/)**

### Demo

[▶️ Watch the Dental AI Receptionist Demo](Dental-AI-receptionist/demo/n8n.mp4)

![Dental AI Receptionist Demo](Dental-AI-receptionist/demo/n8n.gif)

![Dental AI Receptionist](Dental-AI-receptionist/screenshots/Create_event.png)

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
👉 [View the full AI Sales Dashboard project](AI-sales-dashboard/)

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
  
👉 [View the full IT Support Analytics project](IT-Support-Analytics/)
### Dashboard Preview

![Overview Dashboard](IT-Support-Analytics//screenshots/Dashboard.png)


# 🔧 Technology Overview

| Area | Technologies |
|---|---|
| Data & BI | SQL · Power BI · Dremio |
| Databases | PostgreSQL · pgvector · Azure SQL |
| AI | AI Agents · RAG · Embeddings |
| Automation | n8n · Webhooks · APIs |
| Web | Next.js · React · JavaScript |
| Cloud & Deployment | Vercel · Cloudflare Tunnel |
| Productivity | GitHub · Visual Studio Code |
| Integrations | Google Calendar |

# 🎯 Portfolio Focus

These projects demonstrate a progression across **IT Operations → Data Analytics → BI → Automation → AI → RAG → Web Applications**.

The focus is on practical solutions that connect technical infrastructure, data and AI with real business workflows.

---
