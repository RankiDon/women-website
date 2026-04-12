# Feminist Women Website - Design & Technical Specification

## 1. Concept & Vision

A bold, unapologetic digital space for feminist voices that channels Apple's iconic design philosophy—clean, powerful, and transformative. The website feels like stepping into a premium space where ideas matter and stories deserve to be seen. Every interaction communicates: "This is important, and so are you."

## 2. Design Language

### Aesthetic Direction
Inspired by apple.com's iconic "less is more" philosophy—massive typography commands attention, generous whitespace creates breathing room, and subtle animations add life without distraction. The feminist message is amplified through confident, bold design choices.

### Color Palette
- **Primary Background**: `#FFFFFF` (Pure white)
- **Secondary Background**: `#FBFBFD` (Subtle off-white for sections)
- **Text Primary**: `#1D1D1F` (Near black)
- **Text Secondary**: `#86868B` (Medium gray)
- **Accent Blue**: `#0071E3` (Apple blue - links, buttons, highlights)
- **Accent Hover**: `#0077ED` (Darker blue for hover states)
- **Subtle Border**: `#D2D2D7` (Light gray for dividers)
- **Hero Gradient**: `#f5f5f7` (Gradient background)

### Typography
- **Font Family**: `system-ui, -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', sans-serif`
- **Hero Titles**: 96px bold, letter-spacing: -0.02em
- **Section Titles**: 64px bold, letter-spacing: -0.02em
- **Card Titles**: 24px semibold
- **Body Text**: 17px regular, line-height: 1.47
- **Small Text**: 12px regular

### Spatial System
- **Container Max Width**: 980px (centered)
- **Section Padding**: 80px vertical
- **Card Gap**: 24px
- **Component Border Radius**: 18px (cards), 12px (buttons)

### Motion Philosophy
- **Scroll Animations**: Elements fade up with translateY(30px) → translateY(0), opacity 0 → 1, 800ms ease-out
- **Hover Transitions**: 300ms cubic-bezier(0.25, 0.1, 0.25, 1)
- **Page Transitions**: Crossfade 400ms
- **Stagger Delay**: 100ms between sequential items

### Visual Assets
- **Icons**: Lucide Icons (clean, minimal line icons)
- **Images**: High-quality Unsplash images with feminist/women themes
- **Decorative**: Subtle gradients, soft shadows (0 4px 20px rgba(0,0,0,0.08))

## 3. Layout & Structure

### Navigation (Fixed Top)
- Logo "Feminist Women" on left
- Nav links on right: Home, Articles, About, Contact
- Background blur on scroll (backdrop-filter: blur(20px))
- Height: 48px

### Home Page Structure
1. **Hero Section** (100vh)
   - Massive headline with gradient text effect
   - Subheadline with mission statement
   - CTA button to Articles
   - Background: subtle radial gradient

2. **Featured Articles Grid**
   - 3-column grid of article cards
   - Large image, category tag, title, excerpt

3. **Values Section**
   - Full-width with light gray background
   - 4 value propositions in a row
   - Icon + title + description

4. **Latest Articles**
   - 2-column grid with larger cards

5. **Footer**
   - Minimal: copyright + social links

### Articles Page
- Filter bar with category pills
- Grid of article cards (responsive: 3 → 2 → 1 columns)
- Load more button

### Article Detail Page
- Full-width hero image
- Article metadata (category, author, date)
- Rich content area (max 680px centered)
- Related articles section at bottom

### About Page
- Hero with mission statement
- Team member grid
- History/timeline section

### Contact Page
- Clean contact form
- Social links
- Office location (optional)

## 4. Features & Interactions

### Navigation
- Smooth scroll to sections on home page
- Active link highlighting
- Mobile hamburger menu

### Article Cards
- Hover: image scale 1.02, shadow increase, slight lift
- Click: navigate to article detail

### Forms
- Input focus: blue border glow
- Submit: loading state, success/error feedback
- Validation: inline error messages

### Animations
- Intersection Observer for scroll reveal
- Parallax on hero image (subtle)
- Page load sequence

## 5. Component Inventory

### NavBar
- States: default, scrolled (with blur background), mobile-open
- Logo click → home
- Mobile: hamburger → slide-out menu

### HeroSection
- Animated text reveal
- CTA button with hover effect

### ArticleCard
- States: default, hover (elevated), loading (skeleton)
- Image, category badge, title, excerpt, date

### CategoryPill
- States: default, active (filled blue), hover

### Button
- Variants: primary (filled), secondary (outline), ghost
- States: default, hover, active, disabled, loading

### Input/Textarea
- States: default, focus (blue glow), error (red border), disabled
- Floating label animation

### Footer
- Simple centered layout
- Social icon links

## 6. Technical Approach

### Backend (Spring Boot 3.x)
```
Package: com.feminist.women
Port: 8080

Entity Classes:
- Article (id, title, content, category, author, coverImage, createdAt, updatedAt)
- Category (id, name, description)

Mapper Interfaces:
- ArticleMapper
- CategoryMapper

Service Classes:
- ArticleService
- CategoryService

Controller:
- ArticleController (/api/articles)
- CategoryController (/api/categories)
```

### API Endpoints

#### Articles
| Method | Endpoint | Description | Request Body |
|--------|----------|-------------|--------------|
| GET | /api/articles | List articles (paginated) | ?page=0&size=10&category= |
| GET | /api/articles/{id} | Get single article | - |
| POST | /api/articles | Create article | {title, content, category, author, coverImage} |
| PUT | /api/articles/{id} | Update article | {title, content, category, author, coverImage} |
| DELETE | /api/articles/{id} | Delete article | - |

#### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /api/categories | List all categories |

### Database (MySQL)
```
Database: feminist_women

articles table:
- id: BIGINT AUTO_INCREMENT PRIMARY KEY
- title: VARCHAR(255) NOT NULL
- content: TEXT NOT NULL
- category: VARCHAR(100)
- author: VARCHAR(100)
- cover_image: VARCHAR(500)
- created_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
- updated_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE

categories table:
- id: BIGINT AUTO_INCREMENT PRIMARY KEY
- name: VARCHAR(100) NOT NULL UNIQUE
- description: VARCHAR(500)
```

### Frontend (Vue 3 + Vite)
```
Port: 5173

Router Routes:
- / → Home
- /articles → Articles list
- /articles/:id → Article detail
- /about → About
- /contact → Contact

Components:
- NavBar.vue
- HeroSection.vue
- ArticleCard.vue
- ArticleGrid.vue
- CategoryFilter.vue
- ValuesSection.vue
- FooterSection.vue
- ContactForm.vue

Services:
- api.js (axios instance with interceptors)

Stores:
- articles.js (reactive state management)
```

### State Management
- Vue 3 Composition API with reactive refs
- Simple store pattern for articles state

### Error Handling
- Backend: Global exception handler
- Frontend: Axios interceptors for global error handling
- Loading states for all async operations

## 7. Responsive Breakpoints

- **Desktop**: 1024px+
- **Tablet**: 768px - 1023px
- **Mobile**: < 768px

### Mobile Adjustments
- Nav: hamburger menu
- Grid: 3 → 2 → 1 columns
- Typography: scales down proportionally
- Padding: reduced by 50%
