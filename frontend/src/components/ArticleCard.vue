<template>
  <article class="article-card" @click="navigateToArticle">
    <div class="card-image" v-if="article.imageUrl">
      <img :src="article.imageUrl" :alt="article.title" />
    </div>
    <div class="card-image placeholder" v-else>
      <div class="placeholder-icon">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2z"/>
          <path d="M14 17l-5-5 1.41-1.41L14 14.17l7.59-7.59L23 8l-9 9z"/>
        </svg>
      </div>
    </div>
    <div class="card-content">
      <span class="card-category">{{ article.category }}</span>
      <h3 class="card-title">{{ article.title }}</h3>
      <p class="card-excerpt">{{ truncatedExcerpt }}</p>
      <div class="card-meta">
        <span class="card-date">{{ formattedDate }}</span>
        <span class="card-author">{{ article.author }}</span>
      </div>
    </div>
  </article>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const props = defineProps({
  article: {
    type: Object,
    required: true
  }
})

const router = useRouter()

const truncatedExcerpt = computed(() => {
  const excerpt = props.article.content || props.article.excerpt || ''
  return excerpt.length > 120 ? excerpt.substring(0, 120) + '...' : excerpt
})

const formattedDate = computed(() => {
  if (!props.article.createTime) return ''
  const date = new Date(props.article.createTime)
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
})

const navigateToArticle = () => {
  router.push(`/articles/${props.article.id}`)
}
</script>

<style scoped>
.article-card {
  cursor: pointer;
  transition: transform 0.4s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.article-card:hover {
  transform: scale(1.02);
}

.card-image {
  width: 100%;
  aspect-ratio: 16 / 10;
  overflow: hidden;
  background: #f5f5f7;
  border-radius: 12px;
  margin-bottom: 20px;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.article-card:hover .card-image img {
  transform: scale(1.05);
}

.card-image.placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #f5f5f7 0%, #e8e8ed 100%);
}

.placeholder-icon {
  color: #86868b;
}

.card-category {
  display: inline-block;
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-blue);
  margin-bottom: 8px;
}

.card-title {
  font-size: 21px;
  font-weight: 600;
  line-height: 1.3;
  letter-spacing: -0.02em;
  color: var(--color-black);
  margin: 0 0 12px;
}

.card-excerpt {
  font-size: 14px;
  line-height: 1.6;
  color: var(--color-gray);
  margin: 0 0 16px;
}

.card-meta {
  display: flex;
  gap: 16px;
  font-size: 12px;
  color: var(--color-gray);
}

.card-meta span {
  display: flex;
  align-items: center;
}

.card-meta span::after {
  content: '';
  display: none;
}

.card-date::after {
  content: '·';
  margin-left: 16px;
  display: inline-block;
}
</style>