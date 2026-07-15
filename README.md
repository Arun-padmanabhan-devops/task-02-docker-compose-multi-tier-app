# Task 02 - Multi-Tier Application using Docker Compose

## 📌 Project Overview

This project demonstrates how to deploy a multi-tier application using **Docker Compose**.

The application consists of three services:

- 🌐 Frontend - Nginx
- ⚙️ Backend - Python Flask
- 🗄️ Database - MySQL

Docker Compose is used to orchestrate all services, configure networking, manage environment variables, and persist database data using Docker volumes.

---

## 🏗️ Architecture

```
Browser
   │
   ▼
Nginx (Frontend)
   │
   ▼
Flask (Backend)
   │
   ▼
MySQL (Database)
```

---

## 🛠️ Technologies Used

- Docker
- Docker Compose
- Nginx
- Python Flask
- MySQL

---

## 📂 Project Structure

```
task-02-docker-compose-multi-tier-app
├── app
├── web
├── docker-compose.yml
├── README.md
└── .env.example
```

---

## 🚀 Learning Objectives

- Docker Images
- Docker Containers
- Dockerfile
- Docker Compose
- Docker Networking
- Docker Volumes
- Environment Variables

---

## 👨‍💻 Author

Arun