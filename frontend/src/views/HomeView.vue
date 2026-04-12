<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">Empowering Women,<br />Inspiring Change</h1>
        <p class="hero-subtitle">
          Stories, perspectives, and voices that celebrate and advance the feminist movement.
        </p>
        <div class="hero-cta">
          <router-link to="/articles" class="btn-primary">Explore Articles</router-link>
          <router-link to="/about" class="btn-secondary">Learn More</router-link>
        </div>
      </div>
    </section>

    <!-- Featured Articles -->
    <section class="featured">
      <div class="section-container">
        <div class="section-header">
          <h2 class="section-title">Latest Stories</h2>
          <router-link to="/articles" class="section-link">View all</router-link>
        </div>

        <div v-if="loading" class="loading">
          <div class="loading-spinner"></div>
        </div>

        <div v-else-if="articles.length > 0" class="featured-grid">
          <ArticleCard
            v-for="article in articles"
            :key="article.id"
            :article="article"
          />
        </div>

        <div v-else class="empty-state">
          <p>No articles available yet. Check back soon!</p>
        </div>
      </div>
    </section>

    <!-- Mission Section -->
    <section class="mission">
      <div class="mission-content">
        <h2 class="mission-title">Our Mission</h2>
        <p class="mission-text">
          We believe in the power of storytelling to inspire change. Our platform amplifies
          women's voices, explores intersectional feminism, and creates a space for
          honest conversations about gender, equality, and social justice.
        </p>
        <router-link to="/about" class="btn-outline">About Us</router-link>
      </div>
    </section>

    <!-- Categories Section -->
    <section class="categories">
      <div class="section-container">
        <h2 class="section-title center">Explore by Category</h2>
        <div class="categories-grid">
          <router-link
            v-for="category in categories"
            :key="category"
            :to="`/articles?category=${category}`"
            class="category-card"
          >
            <span>{{ category }}</span>
          </router-link>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getArticles, getCategories } from '../api'
import ArticleCard from '../components/ArticleCard.vue'

const articles = ref([])
const categories = ref([])
const loading = ref(true)

const fetchData = async () => {
  try {
    const [articlesRes, categoriesRes] = await Promise.all([
      getArticles(),
      getCategories()
    ])
    articles.value = articlesRes.data.slice(0, 6)
    categories.value = categoriesRes.data
  } catch (error) {
    console.error('Failed to fetch data:', error)
    // Fallback categories if API fails
    categories.value = ['Politics', 'Culture', 'Workplace', 'Health', 'Education', 'Activism']
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchData()
})
</script>

<style scoped>
.home {
  padding-top: 48px;
}

/* Hero Section */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 120px 24px 80px;
  background: linear-gradient(180deg, #f5f5f7 0%, #ffffff 100%);
}

.hero-content {
  max-width: 800px;
  animation: fadeInUp 1s ease-out;
}

.hero-title {
  font-size: clamp(48px, 10vw, 80px);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.03em;
  color: var(--color-black);
  margin: 0 0 24px;
}

.hero-subtitle {
  font-size: clamp(18px, 3vw, 24px);
  font-weight: 400;
  line-height: 1.4;
  color: var(--color-gray);
  margin: 0 0 48px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.hero-cta {
  display: flex;
  gap: 20px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn-primary,
.btn-secondary,
.btn-outline {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 16px 32px;
  font-size: 17px;
  font-weight: 500;
  text-decoration: none;
  border-radius: 980px;
  transition: all 0.3s ease;
}

.btn-primary {
  background: var(--color-black);
  color: var(--color-white);
}

.btn-primary:hover {
  background: #1d1d1f;
  transform: scale(1.02);
}

.btn-secondary {
  background: transparent;
  color: var(--color-black);
  border: 1px solid rgba(0, 0, 0, 0.2);
}

.btn-secondary:hover {
  border-color: var(--color-black);
}

.btn-outline {
  background: transparent;
  color: var(--color-black);
  border: 1px solid var(--color-black);
}

.btn-outline:hover {
  background: var(--color-black);
  color: var(--color-white);
}

/* Featured Section */
.featured {
  padding: 100px 48px;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 60px;
}

.section-title {
  font-size: 40px;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--color-black);
  margin: 0;
}

.section-title.center {
  text-align: center;
  margin-bottom: 60px;
}

.section-link {
  font-size: 17px;
  color: var(--color-blue);
  text-decoration: none;
  font-weight: 500;
}

.section-link:hover {
  text-decoration: underline;
}

.featured-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 40px;
}

.loading {
  display: flex;
  justify-content: center;
  padding: 60px 0;
}

.loading-spinner {
  width: 32px;
  height: 32px;
  border: 3px solid #f5f5f7;
  border-top-color: var(--color-black);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.empty-state {
  text-align: center;
  padding: 60px 0;
  color: var(--color-gray);
  font-size: 17px;
}

/* Mission Section */
.mission {
  padding: 120px 48px;
  background: var(--color-black);
  text-align: center;
}

.mission-content {
  max-width: 700px;
  margin: 0 auto;
}

.mission-title {
  font-size: 48px;
  font-weight: 600;
  letter-spacing: -0.02em;
  color: var(--color-white);
  margin: 0 0 24px;
}

.mission-text {
  font-size: 19px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.8);
  margin: 0 0 40px;
}

/* Categories Section */
.categories {
  padding: 100px 48px;
}

.categories-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.category-card {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  background: #f5f5f7;
  border-radius: 16px;
  text-decoration: none;
  transition: all 0.3s ease;
}

.category-card:hover {
  background: #e8e8ed;
  transform: scale(1.02);
}

.category-card span {
  font-size: 21px;
  font-weight: 600;
  color: var(--color-black);
  letter-spacing: -0.02em;
}

/* Animations */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* Responsive */
@media (max-width: 1024px) {
  .featured-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 100px 24px 60px;
  }

  .featured {
    padding: 60px 24px;
  }

  .section-header {
    flex-direction: column;
    gap: 16px;
    text-align: center;
  }

  .featured-grid {
    grid-template-columns: 1fr;
    gap: 48px;
  }

  .categories {
    padding: 60px 24px;
  }

  .categories-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .mission {
    padding: 80px 24px;
  }

  .mission-title {
    font-size: 36px;
  }
}
</style>