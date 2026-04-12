<template>
  <div class="articles-view">
    <section class="page-header">
      <div class="header-content">
        <h1>文章</h1>
        <p>用故事启发、激励并点燃变革。</p>
      </div>
    </section>

    <section class="articles-content">
      <div class="articles-container">
        <!-- Category Filter -->
        <div class="category-filter">
          <button
            v-for="cat in ['全部', ...categories]"
            :key="cat"
            :class="['filter-btn', { active: selectedCategory === cat }]"
            @click="selectCategory(cat)"
          >
            {{ cat }}
          </button>
        </div>

        <!-- Loading State -->
        <div v-if="loading" class="loading">
          <div class="loading-spinner"></div>
        </div>

        <!-- Articles Grid -->
        <div v-else-if="filteredArticles.length > 0" class="articles-grid">
          <ArticleCard
            v-for="article in filteredArticles"
            :key="article.id"
            :article="article"
          />
        </div>

        <!-- Empty State -->
        <div v-else class="empty-state">
          <p>该分类下暂无文章。</p>
          <button @click="selectCategory('全部')" class="btn-reset">查看全部文章</button>
        </div>

        <!-- Load More -->
        <div v-if="hasMore && !loading" class="load-more">
          <button @click="loadMore" class="btn-load-more">加载更多</button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { getArticles } from '../api'
import ArticleCard from '../components/ArticleCard.vue'

const route = useRoute()
const router = useRouter()

const articles = ref([])
const categories = ref([])
const selectedCategory = ref('全部')
const loading = ref(true)
const currentPage = ref(1)
const pageSize = 9
const hasMore = ref(false)

const filteredArticles = computed(() => {
  if (selectedCategory.value === '全部') {
    return articles.value
  }
  return articles.value.filter(
    article => article.category === selectedCategory.value
  )
})

const fetchArticles = async () => {
  try {
    loading.value = true
    const response = await getArticles({ page: currentPage.value, size: pageSize })
    const newArticles = response.data.articles

    if (currentPage.value === 1) {
      articles.value = newArticles
    } else {
      articles.value = [...articles.value, ...newArticles]
    }

    hasMore.value = newArticles.length === pageSize

    // Extract unique categories
    const uniqueCategories = [...new Set(newArticles.map(a => a.category).filter(Boolean))]
    categories.value = [...new Set([...categories.value, ...uniqueCategories])]
  } catch (error) {
    console.error('Failed to fetch articles:', error)
    // Fallback mock data
    if (currentPage.value === 1) {
      articles.value = [
        { id: 1, title: 'The Future of Feminism', category: 'Politics', content: 'Exploring the evolving landscape of feminist thought...', author: 'Sarah Chen', createdAt: '2026-04-10' },
        { id: 2, title: 'Women in Tech', category: 'Workplace', content: 'Breaking barriers in the technology industry...', author: 'Maria Garcia', createdAt: '2026-04-08' },
        { id: 3, title: 'Reproductive Rights', category: 'Health', content: 'Understanding the ongoing fight for bodily autonomy...', author: 'Dr. Emily Brown', createdAt: '2026-04-05' },
        { id: 4, title: 'Intersectionality 101', category: 'Education', content: 'A beginner guide to intersectional feminism...', author: 'James Wilson', createdAt: '2026-04-01' },
      ]
      categories.value = ['政治', '职场', '健康', '教育']
    }
  } finally {
    loading.value = false
  }
}

const selectCategory = (category) => {
  selectedCategory.value = category
  currentPage.value = 1

  if (category === '全部') {
    router.push({ path: '/articles' })
  } else {
    router.push({ path: '/articles', query: { category } })
  }
}

const loadMore = () => {
  currentPage.value++
  fetchArticles()
}

// Watch for route query changes
watch(
  () => route.query.category,
  (newCategory) => {
    selectedCategory.value = newCategory || '全部'
    currentPage.value = 1
    articles.value = []
    fetchArticles()
  }
)

onMounted(() => {
  const categoryFromUrl = route.query.category
  if (categoryFromUrl) {
    selectedCategory.value = categoryFromUrl
  }
  fetchArticles()
})
</script>

<style scoped>
.articles-view {
  padding-top: 48px;
}

.page-header {
  padding: 100px 48px 60px;
  text-align: center;
  background: linear-gradient(180deg, #f5f5f7 0%, #ffffff 100%);
}

.header-content h1 {
  font-size: 64px;
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--color-black);
  margin: 0 0 16px;
}

.header-content p {
  font-size: 24px;
  color: var(--color-gray);
  margin: 0;
}

.articles-content {
  padding: 80px 48px;
}

.articles-container {
  max-width: 1200px;
  margin: 0 auto;
}

.category-filter {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 60px;
  justify-content: center;
}

.filter-btn {
  padding: 10px 20px;
  font-size: 14px;
  font-weight: 500;
  background: #f5f5f7;
  border: none;
  border-radius: 980px;
  cursor: pointer;
  transition: all 0.3s ease;
  color: var(--color-black);
}

.filter-btn:hover {
  background: #e8e8ed;
}

.filter-btn.active {
  background: var(--color-black);
  color: var(--color-white);
}

.articles-grid {
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
  padding: 80px 0;
}

.empty-state p {
  font-size: 19px;
  color: var(--color-gray);
  margin: 0 0 24px;
}

.btn-reset,
.btn-load-more {
  padding: 14px 28px;
  font-size: 14px;
  font-weight: 500;
  background: var(--color-black);
  color: var(--color-white);
  border: none;
  border-radius: 980px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.btn-reset:hover,
.btn-load-more:hover {
  background: #1d1d1f;
  transform: scale(1.02);
}

.load-more {
  display: flex;
  justify-content: center;
  margin-top: 60px;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 1024px) {
  .articles-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .page-header {
    padding: 80px 24px 40px;
  }

  .header-content h1 {
    font-size: 44px;
  }

  .header-content p {
    font-size: 19px;
  }

  .articles-content {
    padding: 60px 24px;
  }

  .articles-grid {
    grid-template-columns: 1fr;
    gap: 48px;
  }

  .category-filter {
    justify-content: flex-start;
    overflow-x: auto;
    flex-wrap: nowrap;
    padding-bottom: 8px;
    -webkit-overflow-scrolling: touch;
  }

  .filter-btn {
    flex-shrink: 0;
  }
}
</style>