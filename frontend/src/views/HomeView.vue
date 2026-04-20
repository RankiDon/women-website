<template>
  <div class="flower-field-page">
    <!-- Header overlay -->
    <header class="field-header">
      <div class="logo">Women</div>
      <nav class="nav-links">
        <router-link to="/articles">花田</router-link>
        <router-link to="/about">关于</router-link>
        <router-link to="/contact">联系</router-link>
      </nav>
    </header>

    <!-- Title overlay -->
    <div class="field-title">
      <h1>花田</h1>
      <p>每一朵花都是一个故事</p>
    </div>

    <!-- Three.js Flower Field -->
    <ThreeFlowerField v-if="articles.length > 0" :articles="articles" />

    <!-- Loading state -->
    <div v-if="loading" class="loading-overlay">
      <div class="loading-spinner"></div>
      <p>花田生成中...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getArticles } from '../api'
import ThreeFlowerField from '../components/ThreeFlowerField.vue'

const articles = ref([])
const loading = ref(true)

const fetchArticles = async () => {
  try {
    loading.value = true
    const response = await getArticles({ page: 0, size: 50 })
    articles.value = response.data.articles
  } catch (error) {
    console.error('Failed to fetch articles:', error)
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  fetchArticles()
})
</script>

<style scoped>
.flower-field-page {
  min-height: 100vh;
  position: relative;
  background: #1a1a2e;
}

/* Header */
.field-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 32px;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(15px);
  z-index: 1000;
}

.logo {
  font-size: 24px;
  font-weight: 700;
  color: white;
  letter-spacing: -0.02em;
  text-shadow: 0 0 20px rgba(255,255,255,0.5);
}

.nav-links {
  display: flex;
  gap: 24px;
}

.nav-links a {
  text-decoration: none;
  color: white;
  font-size: 14px;
  font-weight: 500;
  padding: 8px 16px;
  border-radius: 20px;
  transition: all 0.3s ease;
  background: rgba(255, 255, 255, 0.1);
}

.nav-links a:hover {
  background: rgba(255, 255, 255, 0.25);
  transform: translateY(-2px);
}

.nav-links a:first-child {
  background: rgba(255, 255, 255, 0.2);
  box-shadow: 0 0 15px rgba(255,255,255,0.3);
}

/* Title */
.field-title {
  position: fixed;
  top: 80px;
  left: 50%;
  transform: translateX(-50%);
  text-align: center;
  z-index: 100;
  pointer-events: none;
}

.field-title h1 {
  font-size: clamp(48px, 12vw, 100px);
  font-weight: 700;
  color: white;
  text-shadow:
    0 0 40px rgba(255,255,255,0.8),
    0 0 80px rgba(255,200,255,0.5),
    0 0 120px rgba(200,150,255,0.3);
  margin: 0;
  letter-spacing: 0.15em;
  animation: glow 3s ease-in-out infinite;
}

.field-title p {
  font-size: clamp(16px, 3vw, 24px);
  color: rgba(255, 255, 255, 0.8);
  text-shadow: 0 0 20px rgba(255,255,255,0.5);
  margin-top: 12px;
  letter-spacing: 0.2em;
}

@keyframes glow {
  0%, 100% { filter: brightness(1); }
  50% { filter: brightness(1.2); }
}

/* Loading */
.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(26, 26, 46, 0.95);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  z-index: 2000;
}

.loading-spinner {
  width: 60px;
  height: 60px;
  border: 4px solid rgba(255, 255, 255, 0.2);
  border-top-color: white;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  box-shadow: 0 0 30px rgba(255,255,255,0.3);
  margin-bottom: 20px;
}

.loading-overlay p {
  color: white;
  font-size: 18px;
  letter-spacing: 0.1em;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Responsive */
@media (max-width: 768px) {
  .field-header {
    padding: 12px 16px;
  }

  .logo {
    font-size: 18px;
  }

  .nav-links {
    gap: 8px;
  }

  .nav-links a {
    padding: 6px 10px;
    font-size: 11px;
  }

  .field-title {
    top: 60px;
  }
}
</style>
