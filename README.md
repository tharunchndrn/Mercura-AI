# Mercura-AI
Mercura AI is an AI-powered e-commerce backend platform that helps online stores automate product management, customer assistance, order workflows, inventory insights, and marketing operations using intelligent AI agents.


# Mercura-AI Agent's Backend

## Overview

This project is the backend service for an AI-powered Ecommerce System built using FastAPI and PostgreSQL.

## Features

- JWT Authentication
- User Management
- Product Management
- Cart Management
- Order Management
- Payment Webhook Structure
- PostgreSQL Database
- Alembic Migrations
- Pytest Testing

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- JWT Authentication
- Pytest

## Installation

### Clone Repository

bash git clone <repository-url> cd backend 

### Create Virtual Environment

bash python -m venv venv source venv/bin/activate 

### Install Dependencies

bash pip install -r requirements.txt 

### Configure Environment Variables

Create a .env file:

env DATABASE_URL=your_database_url SECRET_KEY=your_secret_key 

### Run Database Migrations

bash alembic upgrade head 

### Start Server

bash uvicorn app.main:app --reload 

### Run Tests

bash python -m pytest 

## API Modules

- Authentication
- Users
- Products
- Cart
- Orders
- Payments

## API Documentation

Swagger UI:

text http://127.0.0.1:8000/docs 