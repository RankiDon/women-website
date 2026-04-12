<template>
  <nav class="navbar">
    <div class="navbar-container">
      <router-link to="/" class="navbar-logo">
        <span class="logo-text">Women</span>
      </router-link>

      <button class="navbar-toggle" @click="toggleMenu" :class="{ active: isMenuOpen }">
        <span></span>
        <span></span>
        <span></span>
      </button>

      <ul class="navbar-menu" :class="{ active: isMenuOpen }">
        <li><router-link to="/articles" @click="closeMenu">文章</router-link></li>
        <li><router-link to="/about" @click="closeMenu">关于我们</router-link></li>
        <li><router-link to="/contact" @click="closeMenu">联系我们</router-link></li>
      </ul>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const closeMenu = () => {
  isMenuOpen.value = false
}

const handleScroll = () => {
  const navbar = document.querySelector('.navbar')
  if (window.scrollY > 50) {
    navbar.classList.add('scrolled')
  } else {
    navbar.classList.remove('scrolled')
  }
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  padding: 0 48px;
  transition: all 0.3s ease;
}

.navbar.scrolled {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 48px;
}

.navbar-logo {
  font-size: 21px;
  font-weight: 600;
  color: var(--color-black);
  text-decoration: none;
  letter-spacing: -0.02em;
}

.navbar-menu {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
  gap: 32px;
}

.navbar-menu a {
  font-size: 14px;
  font-weight: 400;
  color: var(--color-black);
  text-decoration: none;
  opacity: 0.8;
  transition: opacity 0.3s ease;
}

.navbar-menu a:hover,
.navbar-menu a.router-link-active {
  opacity: 1;
}

.navbar-toggle {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
}

.navbar-toggle span {
  width: 18px;
  height: 1px;
  background: var(--color-black);
  transition: all 0.3s ease;
}

.navbar-toggle.active span:first-child {
  transform: rotate(45deg) translate(4px, 4px);
}

.navbar-toggle.active span:nth-child(2) {
  opacity: 0;
}

.navbar-toggle.active span:last-child {
  transform: rotate(-45deg) translate(4px, -4px);
}

@media (max-width: 768px) {
  .navbar {
    padding: 0 24px;
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: saturate(180%) blur(20px);
    -webkit-backdrop-filter: saturate(180%) blur(20px);
  }

  .navbar-toggle {
    display: flex;
  }

  .navbar-menu {
    position: fixed;
    top: 48px;
    left: 0;
    right: 0;
    bottom: 0;
    background: var(--color-white);
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 40px;
    opacity: 0;
    visibility: hidden;
    transition: all 0.3s ease;
  }

  .navbar-menu.active {
    opacity: 1;
    visibility: visible;
  }

  .navbar-menu a {
    font-size: 28px;
    font-weight: 500;
    letter-spacing: -0.02em;
  }
}
</style>