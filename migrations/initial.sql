-- initial.sql: create tables in Supabase (PostgreSQL)
-- Author: Roj Padida Jr.

-- ensure uuid generation
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE IF NOT EXISTS customers (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  name text NOT NULL,
  age integer NOT NULL,
  contact_info text,
  is_disabled boolean NOT NULL DEFAULT false,
  medical_conditions text[] DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS rentals (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  customer_id uuid REFERENCES customers(id),
  rental_date timestamptz NOT NULL DEFAULT now(),
  shoe_size numeric NOT NULL,
  rental_fee numeric NOT NULL,
  discount numeric NOT NULL,
  total_fee numeric NOT NULL
);
