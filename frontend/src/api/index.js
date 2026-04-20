import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

// Articles
export const getArticles = (params) => {
  return api.get('/articles', { params })
}

export const getArticleById = (id) => {
  return api.get(`/articles/${id}`)
}

export const getArticlesByCategory = (category) => {
  return api.get('/articles', { params: { category } })
}

export const getCategories = () => {
  return api.get('/categories')
}

// Contact
export const submitContact = (data) => {
  return api.post('/contact', data)
}

export default api