# Bowling Shoes Rental Service API

**Built by Rogelio "Roj" Padida Jr.**

A FastAPI backend managing customers and rentals, with LLM-driven discount logic.

---

## Features

- **Customer Management**: create & list customers  
- **Shoe Rentals**: record rentals, calculate discounts, compute total fee  
- **LLM Integration**: uses OpenAI to pick highest discount via prompt engineering  
- **Supabase**: PostgreSQL database via Supabase Python SDK  
- **Swagger UI**: interactive docs at `/docs`  

---

## Setup

1. **Clone**  
   ```bash
   git clone <your-repo-url>
   cd <repo>
Environment
Create a .env in project root:

env
Copy
SUPABASE_URL=https://xyzcompany.supabase.co
SUPABASE_API_KEY=your-supabase-key
LLM_API_KEY=your-openai-key
Database Migration

bash
Copy
psql $SUPABASE_URL -U postgres -f migrations/initial.sql
Run Locally

bash
Copy
docker-compose up --build
API available at http://localhost:8000

Swagger: http://localhost:8000/docs

API Endpoints

Method	Path	Body	Response
POST	/customers	{ name, age, contact_info, is_disabled, medical_conditions }	new Customer
GET	/customers	—	list[Customer]
POST	/rentals	{ customer_id, shoe_size, rental_fee }	new Rental
GET	/rentals	—	list[Rental]
Design Choices
Supabase SDK: for minimalist CRUD without full ORM

Prompt Engineering: explicit, rule-based prompt to minimize misclassification

Async LLM Calls: keeps FastAPI endpoints non-blocking

Dockerized: single container for easy deployment

Testing with Postman
Import the included postman_collection.json.

Set base_url environment variable to http://localhost:8000.

Run requests in order: Create Customer → Create Rental → List endpoints.

Thanks for reviewing my take-home exam!
— Roj