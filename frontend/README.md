# Women - Feminist Voices Frontend

A Vue 3 frontend for the Women feminist empowerment website, featuring Apple-inspired design with smooth animations and minimalist aesthetics.

## Features

- **Apple-inspired Design**: Clean, minimalist UI with large typography and smooth animations
- **Responsive**: Mobile-first approach that looks great on all devices
- **Vue 3 + Composition API**: Modern Vue patterns with `<script setup>`
- **Vue Router**: Client-side routing with smooth transitions
- **Axios**: API integration with the Spring Boot backend

## Tech Stack

- Vue 3.5
- Vue Router 4.6
- Axios 1.15
- Vite 8.0

## Prerequisites

- Node.js 18+ installed
- Backend server running at http://localhost:8080

## Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies (already done):
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

4. Open your browser to the URL shown (typically http://localhost:5173)

## Project Structure

```
frontend/
├── src/
│   ├── api/
│   │   └── index.js         # Axios API calls
│   ├── components/
│   │   ├── NavBar.vue       # Navigation component
│   │   ├── Footer.vue       # Footer component
│   │   └── ArticleCard.vue  # Article preview card
│   ├── views/
│   │   ├── HomeView.vue     # Homepage with hero
│   │   ├── ArticlesView.vue # Articles list
│   │   ├── ArticleDetailView.vue
│   │   ├── AboutView.vue    # About feminism
│   │   └── ContactView.vue  # Contact form
│   ├── router/
│   │   └── index.js         # Vue Router setup
│   ├── App.vue
│   ├── main.js
│   └── style.css            # Global styles
├── index.html
├── package.json
└── vite.config.js
```

## Pages

- **/** - Homepage with hero, featured articles, and categories
- **/articles** - All articles with category filtering
- **/articles/:id** - Individual article view
- **/about** - About feminism page
- **/contact** - Contact form

## API Endpoints

The frontend connects to the backend at `http://localhost:8080/api`:

- `GET /api/articles` - List all articles
- `GET /api/articles/:id` - Get single article
- `GET /api/categories` - List categories
- `POST /api/contact` - Submit contact form

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## Design

Apple-inspired aesthetic featuring:
- Full-width hero sections
- Large, bold typography (SF Pro-inspired)
- Smooth scroll animations
- Card-based layouts
- White/black/blue color scheme
- Responsive breakpoints at 768px and 1024px
