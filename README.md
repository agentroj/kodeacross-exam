# Bowling Shoes Rental Service API

**Built by Rogelio "Roj" Padida Jr.**

A FastAPI backend managing customers and rentals, with LLM-driven discount logic.

---

## Features

- **Customer Management**: Create & list customers  
- **Shoe Rentals**: Record rentals, calculate discounts, compute total fee  
- **LLM Integration**: Uses OpenAI to pick the highest discount via prompt engineering  
- **Supabase**: PostgreSQL database via Supabase Python SDK  
- **Swagger UI**: Interactive docs at `/docs`  

---

## Setup

1. **Clone**  
   ```bash
   git clone <your-repo-url>
   cd <repo>


## Create `.env`

Create a `.env` file in the project root:

```env
SUPABASE_URL=https://xyzcompany.supabase.co
SUPABASE_API_KEY=your-supabase-key
LLM_API_KEY=your-openai-key
```

## Database Migration

Run the migration:

```bash
psql $SUPABASE_URL -U postgres -f migrations/initial.sql
```

## Run Locally

Build and run with Docker:

```bash
docker-compose up --build
```

## API available at

[http://localhost:8000](http://localhost:8000)

Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## API Endpoints

| Method | Path           | Body                                                                 | Response       |
|--------|----------------|----------------------------------------------------------------------|---------------|
| POST   | /customers     | `{ name, age, contact_info, is_disabled, medical_conditions }`       | new Customer  |
| GET    | /customers     | —                                                                    | list[Customer]|
| POST   | /rentals       | `{ customer_id, shoe_size, rental_fee }`                             | new Rental    |
| GET    | /rentals       | —                                                                    | list[Rental]  |

---

## Design Choices

- **Supabase SDK**: For minimalist CRUD without full ORM  
- **Prompt Engineering**: Explicit, rule-based prompt to minimize misclassification  
- **Async LLM Calls**: Keeps FastAPI endpoints non-blocking  
- **Dockerized**: Single container for easy deployment  

---

## Testing with Postman

1. Import the included `postman_collection.json`.
2. Set the `base_url` environment variable to `http://localhost:8000`.
3. Run requests in order:  
   - Create Customer → Create Rental → List endpoints.

---

Thanks for reviewing my take-home exam!  
— Roj

