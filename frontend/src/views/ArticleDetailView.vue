<template>
  <div class="article-detail">
    <!-- Loading State -->
    <div v-if="loading" class="loading-state">
      <div class="loading-spinner"></div>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="error-state">
      <h2>Article not found</h2>
      <router-link to="/articles" class="btn-back">Back to Articles</router-link>
    </div>

    <!-- Article Content -->
    <article v-else class="article">
      <header class="article-header">
        <div class="header-content">
          <span class="article-category">{{ article.category }}</span>
          <h1 class="article-title">{{ article.title }}</h1>
          <div class="article-meta">
            <span class="article-author">By {{ article.author }}</span>
            <span class="article-date">{{ formattedDate }}</span>
          </div>
        </div>
      </header>

      <div v-if="article.imageUrl" class="article-hero-image">
        <img :src="article.imageUrl" :alt="article.title" />
      </div>

      <div class="article-body">
        <div class="article-content" v-html="formattedContent"></div>

        <aside class="article-sidebar">
          <div class="share-section">
            <h4>Share this article</h4>
            <div class="share-buttons">
              <button @click="shareTwitter" class="share-btn">Twitter</button>
              <button @click="shareFacebook" class="share-btn">Facebook</button>
              <button @click="copyLink" class="share-btn">Copy Link</button>
            </div>
          </div>
        </aside>
      </div>

      <footer class="article-footer">
        <router-link to="/articles" class="btn-back">
          <span>&larr;</span> Back to Articles
        </router-link>
      </footer>
    </article>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { getArticleById } from '../api'

const route = useRoute()
const article = ref({})
const loading = ref(true)
const error = ref(false)

const formattedDate = computed(() => {
  if (!article.value.createTime) return ''
  const date = new Date(article.value.createTime)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
})

const formattedContent = computed(() => {
  // Convert line breaks to paragraphs and escape HTML
  if (!article.value.content) return ''
  const escaped = article.value.content
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
  return escaped.split('\n\n').map(p => `<p>${p}</p>`).join('')
})

const fetchArticle = async () => {
  try {
    loading.value = true
    const response = await getArticleById(route.params.id)
    article.value = response.data
  } catch (err) {
    console.error('Failed to fetch article:', err)
    error.value = true
    // Fallback for demo
    article.value = {
      id: route.params.id,
      title: 'The Future of Feminism',
      category: 'Politics',
      author: 'Sarah Chen',
      createTime: '2026-04-10',
      content: `The feminist movement has always evolved to meet the challenges of its time. From the suffragettes fighting for the right to vote to the modern intersectional movement, each generation has built upon the foundations laid by those who came before.

Today, we stand at a pivotal moment. The fight for gender equality has expanded to encompass a broader understanding of identity, experience, and systemic oppression. We recognize that feminism cannot be monolithic—it must be inclusive, acknowledging the ways race, class, sexuality, and ability intersect with gender.

Technology has transformed how we organize and advocate. Social media has given voice to millions who were previously marginalized, allowing movements like #MeToo to spark global conversations about sexual harassment and assault.

Yet challenges remain. Pay equity, reproductive rights, representation in leadership, and ending violence against women are all battles still being fought. The future of feminism depends on our ability to build coalitions, center the most vulnerable, and remain vigilant in the face of backlash.

This is not just a women's issue—it is a human issue. When we lift women up, we lift entire communities. The future is feminist, and that future is being written by all of us.`,
      imageUrl: null
    }
  } finally {
    loading.value = false
  }
}

const shareTwitter = () => {
  const text = encodeURIComponent(article.value.title)
  const url = encodeURIComponent(window.location.href)
  window.open(`https://twitter.com/intent/tweet?text=${text}&url=${url}`, '_blank')
}

const shareFacebook = () => {
  const url = encodeURIComponent(window.location.href)
  window.open(`https://www.facebook.com/sharer/sharer.php?u=${url}`, '_blank')
}

const copyLink = async () => {
  try {
    await navigator.clipboard.writeText(window.location.href)
    alert('Link copied to clipboard!')
  } catch (err) {
    console.error('Failed to copy:', err)
  }
}

onMounted(() => {
  fetchArticle()
})
</script>

<style scoped>
.article-detail {
  padding-top: 48px;
}

.loading-state,
.error-state {
  min-height: 80vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.loading-spinner {
  width: 32px;
  height: 32px;
  border: 3px solid #f5f5f7;
  border-top-color: var(--color-black);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

.error-state h2 {
  font-size: 32px;
  color: var(--color-black);
  margin-bottom: 24px;
}

.article-header {
  padding: 100px 48px 60px;
  text-align: center;
  background: linear-gradient(180deg, #f5f5f7 0%, #ffffff 100%);
}

.header-content {
  max-width: 800px;
  margin: 0 auto;
}

.article-category {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-blue);
  margin-bottom: 16px;
}

.article-title {
  font-size: clamp(36px, 6vw, 56px);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.03em;
  color: var(--color-black);
  margin: 0 0 24px;
}

.article-meta {
  display: flex;
  gap: 24px;
  justify-content: center;
  font-size: 14px;
  color: var(--color-gray);
}

.article-hero-image {
  max-width: 1000px;
  margin: 0 auto 60px;
  padding: 0 48px;
}

.article-hero-image img {
  width: 100%;
  border-radius: 12px;
}

.article-body {
  display: grid;
  grid-template-columns: 1fr 280px;
  gap: 80px;
  max-width: 1100px;
  margin: 0 auto;
  padding: 0 48px 80px;
}

.article-content {
  font-size: 19px;
  line-height: 1.7;
  color: var(--color-black);
}

.article-content :deep(p) {
  margin: 0 0 24px;
}

.article-sidebar {
  position: sticky;
  top: 100px;
  height: fit-content;
}

.share-section {
  padding: 24px;
  background: #f5f5f7;
  border-radius: 12px;
}

.share-section h4 {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-gray);
  margin: 0 0 16px;
}

.share-buttons {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.share-btn {
  padding: 10px 16px;
  font-size: 14px;
  font-weight: 500;
  background: var(--color-white);
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-align: left;
}

.share-btn:hover {
  background: var(--color-black);
  color: var(--color-white);
  border-color: var(--color-black);
}

.article-footer {
  max-width: 800px;
  margin: 0 auto;
  padding: 0 48px 100px;
}

.btn-back {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 17px;
  font-weight: 500;
  color: var(--color-blue);
  text-decoration: none;
  transition: opacity 0.3s ease;
}

.btn-back:hover {
  opacity: 0.7;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

@media (max-width: 768px) {
  .article-header {
    padding: 80px 24px 40px;
  }

  .article-hero-image {
    padding: 0 24px;
  }

  .article-body {
    grid-template-columns: 1fr;
    gap: 40px;
    padding: 0 24px 60px;
  }

  .article-sidebar {
    position: static;
    order: -1;
  }

  .share-buttons {
    flex-direction: row;
    flex-wrap: wrap;
  }

  .share-btn {
    flex: 1;
    min-width: 100px;
    text-align: center;
  }

  .article-footer {
    padding: 0 24px 60px;
  }
}
</style>