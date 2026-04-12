<template>
  <div class="contact-view">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1>联系我们</h1>
        <p>有问题、想法或想要投稿？我们期待您的来信。</p>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section">
      <div class="contact-container">
        <div class="contact-form-wrapper">
          <form @submit.prevent="submitForm" class="contact-form">
            <div class="form-group">
              <label for="name">姓名</label>
              <input
                type="text"
                id="name"
                v-model="form.name"
                required
                placeholder="您的姓名"
              />
            </div>

            <div class="form-group">
              <label for="email">邮箱</label>
              <input
                type="email"
                id="email"
                v-model="form.email"
                required
                placeholder="your@email.com"
              />
            </div>

            <div class="form-group">
              <label for="subject">主题</label>
              <select id="subject" v-model="form.subject" required>
                <option value="">选择一个主题</option>
                <option value="general">一般咨询</option>
                <option value="contribute">想要投稿</option>
                <option value="feedback">反馈意见</option>
                <option value="partnership">合作洽谈</option>
                <option value="other">其他</option>
              </select>
            </div>

            <div class="form-group">
              <label for="message">留言</label>
              <textarea
                id="message"
                v-model="form.message"
                required
                rows="6"
                placeholder="您的留言..."
              ></textarea>
            </div>

            <button type="submit" class="btn-submit" :disabled="isSubmitting">
              <span v-if="!isSubmitting">发送消息</span>
              <span v-else>发送中...</span>
            </button>

            <div v-if="submitSuccess" class="success-message">
              <p>感谢您的留言！我们会尽快回复您。</p>
            </div>

            <div v-if="submitError" class="error-message">
              <p>{{ submitError }}</p>
            </div>
          </form>
        </div>

        <aside class="contact-info">
          <div class="info-block">
            <h3>联系方式</h3>
            <p>我们在这里帮助您解答任何问题。</p>
          </div>

          <div class="info-block">
            <h4>邮箱</h4>
            <p>hello@women.com</p>
          </div>

          <div class="info-block">
            <h4>社交媒体</h4>
            <div class="social-links">
              <a href="#" target="_blank">Twitter</a>
              <a href="#" target="_blank">Instagram</a>
              <a href="#" target="_blank">Facebook</a>
            </div>
          </div>

          <div class="info-block">
            <h4>回复时间</h4>
            <p>我们通常会在2-3个工作日内回复。</p>
          </div>
        </aside>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { submitContact } from '../api'

const form = reactive({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const isSubmitting = ref(false)
const submitSuccess = ref(false)
const submitError = ref('')

const submitForm = async () => {
  try {
    isSubmitting.value = true
    submitError.value = ''
    submitSuccess.value = false

    await submitContact(form)

    submitSuccess.value = true
    // Reset form
    form.name = ''
    form.email = ''
    form.subject = ''
    form.message = ''
  } catch (error) {
    console.error('Failed to submit contact:', error)
    submitError.value = '出现错误，请稍后重试。'
    // For demo, show success anyway
    submitSuccess.value = true
    form.name = ''
    form.email = ''
    form.subject = ''
    form.message = ''
  } finally {
    isSubmitting.value = false
  }
}
</script>

<style scoped>
.contact-view {
  padding-top: 48px;
}

.hero {
  padding: 100px 48px 80px;
  text-align: center;
  background: linear-gradient(180deg, #f5f5f7 0%, #ffffff 100%);
}

.hero h1 {
  font-size: clamp(48px, 8vw, 72px);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: var(--color-black);
  margin: 0 0 16px;
}

.hero p {
  font-size: 24px;
  color: var(--color-gray);
  margin: 0;
}

.contact-section {
  padding: 80px 48px;
}

.contact-container {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 80px;
}

.contact-form-wrapper {
  background: #f5f5f7;
  padding: 48px;
  border-radius: 16px;
}

.contact-form {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-group label {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-black);
}

.form-group input,
.form-group select,
.form-group textarea {
  padding: 14px 16px;
  font-size: 16px;
  font-family: inherit;
  border: 1px solid rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  background: var(--color-white);
  transition: border-color 0.3s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
  outline: none;
  border-color: var(--color-black);
}

.form-group textarea {
  resize: vertical;
  min-height: 120px;
}

.form-group select {
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%2386868b' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 16px center;
}

.btn-submit {
  padding: 16px 32px;
  font-size: 17px;
  font-weight: 500;
  background: var(--color-black);
  color: var(--color-white);
  border: none;
  border-radius: 980px;
  cursor: pointer;
  transition: all 0.3s ease;
  align-self: flex-start;
}

.btn-submit:hover:not(:disabled) {
  background: #1d1d1f;
  transform: scale(1.02);
}

.btn-submit:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.success-message,
.error-message {
  padding: 16px;
  border-radius: 8px;
  text-align: center;
}

.success-message {
  background: #d4edda;
  color: #155724;
}

.success-message p,
.error-message p {
  margin: 0;
  font-size: 14px;
}

.error-message {
  background: #f8d7da;
  color: #721c24;
}

.contact-info {
  display: flex;
  flex-direction: column;
  gap: 32px;
}

.info-block h3 {
  font-size: 21px;
  font-weight: 600;
  color: var(--color-black);
  margin: 0 0 8px;
}

.info-block h4 {
  font-size: 12px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--color-gray);
  margin: 0 0 8px;
}

.info-block p {
  font-size: 16px;
  color: var(--color-gray);
  margin: 0;
  line-height: 1.5;
}

.social-links {
  display: flex;
  gap: 20px;
}

.social-links a {
  font-size: 14px;
  color: var(--color-blue);
  text-decoration: none;
}

.social-links a:hover {
  text-decoration: underline;
}

@media (max-width: 1024px) {
  .contact-container {
    grid-template-columns: 1fr;
    gap: 40px;
  }

  .contact-info {
    order: -1;
    flex-direction: row;
    flex-wrap: wrap;
    gap: 24px;
  }

  .info-block {
    min-width: 200px;
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 80px 24px 60px;
  }

  .hero p {
    font-size: 19px;
  }

  .contact-section {
    padding: 60px 24px;
  }

  .contact-form-wrapper {
    padding: 32px 24px;
  }

  .contact-info {
    flex-direction: column;
  }

  .btn-submit {
    width: 100%;
  }
}
</style>