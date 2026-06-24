# Shopify ZIP Pricing App

## Overview

This project was built as part of a Shopify development assignment to demonstrate the integration of a Shopify storefront with a custom backend service.

The solution allows customers to enter a ZIP code on a product page and receive location-based pricing dynamically without reloading the page.

The project combines Shopify Theme App Extensions, Shopify App Proxies, FastAPI, and Render deployment into a complete end-to-end solution.

---

## Problem Statement

Different locations may require different pricing rules based on shipping costs, regional promotions, inventory considerations, or business requirements.

The goal of this project was to create a simple and scalable mechanism that:

- Collects a customer's ZIP code
- Sends it to a backend service
- Calculates the appropriate price
- Displays the result directly on the product page

---

## Solution Architecture

```text
Customer
    ↓
Shopify Product Page
    ↓
Theme App Extension (Liquid + JavaScript)
    ↓
Shopify App Proxy
    ↓
FastAPI Backend (Render)
    ↓
JSON Response
    ↓
Theme App Extension
    ↓
Updated Price Display
```

---

## How It Works

### 1. Customer Interaction

A ZIP Pricing Widget is displayed on the Shopify product page.

The customer enters a ZIP code and clicks **Check Price**.

### 2. Frontend Processing

The Theme App Extension contains:

- Liquid markup
- HTML structure
- JavaScript logic

The JavaScript captures the ZIP code entered by the customer and sends a request to the Shopify App Proxy.

Example:

```javascript
fetch("/apps/zip-pricing?zip_code=75028")
```

### 3. Shopify App Proxy

Instead of calling the backend directly, requests pass through Shopify's App Proxy.

Benefits:

- Cleaner architecture
- Backend URL is hidden from storefront code
- Requests appear to originate from the Shopify store

Example route:

```text
/apps/zip-pricing
```

### 4. Backend Processing

The App Proxy forwards the request to a FastAPI application deployed on Render.

The backend:

- Receives the ZIP code
- Applies pricing logic
- Returns a JSON response

Example:

```json
{
  "price": 1499
}
```

### 5. Dynamic Update

JavaScript receives the JSON response and updates the page without requiring a refresh.

The customer immediately sees the location-specific price.

---

## Technologies Used

### Shopify

- Shopify CLI
- Shopify Theme App Extensions
- Shopify App Proxy
- Liquid

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Python
- FastAPI

### Deployment

- Render

### Development Environment

- GitHub Codespaces
- GitHub

---

## Project Structure

```text
shopify-zip-pricing-demo/
│
├── main.py
├── requirements.txt
├── README.md
│
├── shopify_files/
│   ├── shopify.app.toml
│   └── star_rating.liquid
│
└── zip-pricing-app/
```

---

## What I Learned

This project helped me understand several important Shopify concepts beyond simply writing code.

### Shopify Apps vs Themes

A Shopify Theme controls the appearance of the storefront.

A Shopify App provides additional functionality.

Theme App Extensions allow app functionality to be integrated into the storefront without modifying theme source files directly.

---

### Theme App Extensions

I learned how Shopify uses Theme App Extensions to inject functionality into storefront pages.

The ZIP Pricing Widget was implemented using a Theme App Extension and added through the Shopify Theme Editor.

---

### Shopify App Proxies

One of the most valuable concepts learned during this project was Shopify App Proxies.

Instead of exposing backend endpoints directly to the storefront, Shopify can act as a secure intermediary.

```text
Storefront
    ↓
Shopify App Proxy
    ↓
Backend Service
```

This creates a cleaner and more production-ready architecture.

---

### FastAPI

I gained practical experience building API endpoints with FastAPI and returning structured JSON responses that could be consumed by Shopify storefront code.

---

### Cloud Deployment

The backend was deployed to Render, allowing the Shopify storefront to communicate with a publicly accessible API.

---

## Design Decisions

### Why FastAPI?

FastAPI provides:

- Simple API development
- High performance
- Automatic validation
- Easy deployment

### Why App Proxy?

Using Shopify App Proxy:

- Keeps backend architecture separated
- Avoids exposing backend URLs in storefront code
- Aligns with Shopify best practices

### Why Theme App Extension?

Theme App Extensions are Shopify's recommended approach for storefront customization because they:

- Are easy to install
- Are easy to remove
- Work across themes
- Avoid direct theme modifications

---

## Future Improvements

For a production implementation, several enhancements could be added:

- Database-driven ZIP pricing
- Merchant pricing dashboard
- Advanced validation
- Error handling improvements
- Request authentication
- Analytics and reporting
- Caching for faster lookups

---

## Assignment Reflection

The objective of this assignment was not only to build a working solution but also to understand the architecture behind Shopify applications.

Through this project I gained hands-on experience with:

- Shopify App Development
- Theme App Extensions
- Shopify App Proxies
- API Design
- FastAPI
- Cloud Deployment
- Frontend and Backend Integration

Most importantly, I developed a much deeper understanding of how Shopify storefronts communicate with external services while maintaining a clean and scalable architecture.

---

## Author

**Abhinraj**

Built as part of a Shopify development assignment to demonstrate Shopify app architecture, storefront customization, API integration, and backend deployment.
