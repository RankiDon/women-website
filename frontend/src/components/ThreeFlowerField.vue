<template>
  <div ref="container" class="three-container"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import * as THREE from 'three'
import { useRouter } from 'vue-router'

const props = defineProps({
  articles: { type: Array, required: true }
})

const container = ref(null)
const router = useRouter()

let scene, camera, renderer, animationId
let flowers = []
let raycaster, mouse
let hoveredFlower = null
let cameraAngle = 0

// Colors by category
const C = {
  '政治': { p: 0xe74c3c, c: 0xf5b041 },  // red rose
  'Politics': { p: 0xe74c3c, c: 0xf5b041 },
  '健康': { p: 0xff69b4, c: 0xfde8d7 },  // pink tulip
  'Health': { p: 0xff69b4, c: 0xfde8d7 },
  '教育': { p: 0x3498db, c: 0x85c1e9 },  // blue hyacinth
  'Education': { p: 0x3498db, c: 0x85c1e9 },
  '职场': { p: 0xe67e22, c: 0xfef9e7 },  // orange lily
  'Workplace': { p: 0xe67e22, c: 0xfef9e7 },
  '文化': { p: 0x9b59b6, c: 0xe8daef },  // purple lavender
  'Culture': { p: 0x9b59b6, c: 0xe8daef },
  '行动主义': { p: 0xf1c40f, c: 0x8b4513 }, // yellow sunflower
  'Activism': { p: 0xf1c40f, c: 0x8b4513 },
}

// Create a 3D flower with stem, leaves, petals, center
const createFlower = (article, index) => {
  const group = new THREE.Group()
  const colors = C[article.category] || { p: 0xe91e63, c: 0xffc107 }

  // Random natural position
  const angle = Math.random() * Math.PI * 2
  const radius = 3 + Math.random() * 12
  group.position.set(
    Math.cos(angle) * radius + (Math.random() - 0.5) * 3,
    0,
    Math.sin(angle) * radius * 0.6 + (Math.random() - 0.5) * 3
  )
  group.rotation.y = Math.random() * Math.PI * 2

  // Stem - green cylinder
  const stemGeo = new THREE.CylinderGeometry(0.05, 0.07, 2.5, 8)
  const stemMat = new THREE.MeshLambertMaterial({ color: 0x228b22 })
  const stem = new THREE.Mesh(stemGeo, stemMat)
  stem.position.y = 1.25
  stem.castShadow = true
  group.add(stem)

  // Leaves - custom shape
  const leafShape = new THREE.Shape()
  leafShape.moveTo(0, 0)
  leafShape.quadraticCurveTo(0.3, 0.1, 0.8, 0.2)
  leafShape.quadraticCurveTo(1.0, 0.1, 1.2, 0)
  leafShape.quadraticCurveTo(0.8, -0.1, 0.3, -0.1)
  leafShape.quadraticCurveTo(0.1, -0.05, 0, 0)

  const leafGeo = new THREE.ShapeGeometry(leafShape)
  const leafMat = new THREE.MeshLambertMaterial({ color: 0x32cd32, side: THREE.DoubleSide })

  const leaf1 = new THREE.Mesh(leafGeo, leafMat)
  leaf1.position.set(0.3, 1.0, 0.1)
  leaf1.rotation.y = Math.PI / 4
  leaf1.rotation.x = -0.3
  group.add(leaf1)

  const leaf2 = new THREE.Mesh(leafGeo, leafMat)
  leaf2.position.set(-0.3, 1.5, 0.1)
  leaf2.rotation.y = -Math.PI / 3
  leaf2.rotation.x = -0.3
  group.add(leaf2)

  // Flower head group
  const flowerHead = new THREE.Group()
  flowerHead.position.y = 2.6

  // Petals - sphere geometry scaled
  const petalCount = 8
  for (let i = 0; i < petalCount; i++) {
    const angle = (i / petalCount) * Math.PI * 2
    const petalGeo = new THREE.SphereGeometry(0.25, 12, 12)
    petalGeo.scale(1, 1.5, 0.3)
    const petalMat = new THREE.MeshLambertMaterial({ color: colors.p, side: THREE.DoubleSide })
    const petal = new THREE.Mesh(petalGeo, petalMat)
    petal.position.x = Math.cos(angle) * 0.35
    petal.position.z = Math.sin(angle) * 0.35
    petal.rotation.y = -angle + Math.PI / 2
    petal.rotation.x = 0.3
    flowerHead.add(petal)
  }

  // Center - sphere
  const centerGeo = new THREE.SphereGeometry(0.2, 12, 12)
  const centerMat = new THREE.MeshLambertMaterial({ color: colors.c })
  const center = new THREE.Mesh(centerGeo, centerMat)
  center.position.y = 0.1
  flowerHead.add(center)

  group.add(flowerHead)

  // Store data for animation
  group.userData = {
    article,
    flowerHead,
    originalY: group.position.y,
    phase: Math.random() * Math.PI * 2,
    rotationSpeed: 0.3 + Math.random() * 0.4
  }

  return group
}

const initScene = () => {
  const w = container.value.clientWidth
  const h = container.value.clientHeight

  // Scene - dark night background
  scene = new THREE.Scene()
  scene.background = new THREE.Color(0x0a0a1a)
  scene.fog = new THREE.Fog(0x0a0a1a, 15, 50)

  // Camera
  camera = new THREE.PerspectiveCamera(60, w / h, 0.1, 1000)
  camera.position.set(0, 12, 15)
  camera.lookAt(0, 0, 0)

  // Renderer
  renderer = new THREE.WebGLRenderer({ antialias: true })
  renderer.setSize(w, h)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.shadowMap.enabled = true
  renderer.shadowMap.type = THREE.PCFSoftShadowMap
  container.value.appendChild(renderer.domElement)

  // Ambient light
  const ambientLight = new THREE.AmbientLight(0x404060, 0.5)
  scene.add(ambientLight)

  // Moon light (directional)
  const moonLight = new THREE.DirectionalLight(0x8888ff, 0.8)
  moonLight.position.set(5, 15, 5)
  moonLight.castShadow = true
  moonLight.shadow.mapSize.width = 2048
  moonLight.shadow.mapSize.height = 2048
  moonLight.shadow.camera.near = 0.5
  moonLight.shadow.camera.far = 50
  moonLight.shadow.camera.left = -20
  moonLight.shadow.camera.right = 20
  moonLight.shadow.camera.top = 20
  moonLight.shadow.camera.bottom = -20
  scene.add(moonLight)

  // Fill light
  const fillLight = new THREE.PointLight(0xffaaff, 0.3)
  fillLight.position.set(-5, 5, -5)
  scene.add(fillLight)

  // Stars
  const starsGeometry = new THREE.BufferGeometry()
  const starsCount = 2000
  const positions = new Float32Array(starsCount * 3)
  for (let i = 0; i < starsCount * 3; i += 3) {
    positions[i] = (Math.random() - 0.5) * 200
    positions[i + 1] = Math.random() * 100 + 20
    positions[i + 2] = (Math.random() - 0.5) * 200
  }
  starsGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3))
  const starsMaterial = new THREE.PointsMaterial({
    color: 0xffffff,
    size: 0.3,
    transparent: true,
    opacity: 0.8
  })
  const stars = new THREE.Points(starsGeometry, starsMaterial)
  scene.add(stars)

  // Ground - green plane
  const groundGeometry = new THREE.PlaneGeometry(100, 100, 50, 50)
  const positions2 = groundGeometry.attributes.position.array
  for (let i = 0; i < positions2.length; i += 3) {
    positions2[i + 2] += Math.random() * 0.2
  }
  groundGeometry.computeVertexNormals()
  const groundMaterial = new THREE.MeshLambertMaterial({ color: 0x228b22 })
  const ground = new THREE.Mesh(groundGeometry, groundMaterial)
  ground.rotation.x = -Math.PI / 2
  ground.position.y = -0.5
  ground.receiveShadow = true
  scene.add(ground)

  // Grass blades - green triangles
  const grassGeometry = new THREE.BufferGeometry()
  const grassCount = 5000
  const grassPositions = new Float32Array(grassCount * 3)
  const grassColors = new Float32Array(grassCount * 3)

  for (let i = 0; i < grassCount * 3; i += 9) {
    const x = (Math.random() - 0.5) * 50
    const z = (Math.random() - 0.5) * 30
    const height = 0.3 + Math.random() * 0.3

    grassPositions[i] = x
    grassPositions[i + 1] = 0
    grassPositions[i + 2] = z

    grassPositions[i + 3] = x + (Math.random() - 0.5) * 0.1
    grassPositions[i + 4] = height
    grassPositions[i + 5] = z

    grassPositions[i + 6] = x + (Math.random() - 0.5) * 0.1
    grassPositions[i + 7] = height * 0.8
    grassPositions[i + 8] = z + 0.1

    const green = 0.3 + Math.random() * 0.2
    grassColors[i] = 0.1
    grassColors[i + 1] = green
    grassColors[i + 2] = 0.1
    grassColors[i + 3] = 0.15
    grassColors[i + 4] = green + 0.1
    grassColors[i + 5] = 0.15
    grassColors[i + 6] = 0.1
    grassColors[i + 7] = green
    grassColors[i + 8] = 0.1
  }

  grassGeometry.setAttribute('position', new THREE.BufferAttribute(grassPositions, 3))
  grassGeometry.setAttribute('color', new THREE.BufferAttribute(grassColors, 3))

  const grassMaterial = new THREE.MeshBasicMaterial({
    vertexColors: true,
    side: THREE.DoubleSide
  })
  const grass = new THREE.Mesh(grassGeometry, grassMaterial)
  scene.add(grass)

  // Raycaster for interaction
  raycaster = new THREE.Raycaster()
  mouse = new THREE.Vector2()

  createFlowers()
}

const createFlowers = () => {
  flowers.forEach(f => scene.remove(f))
  flowers = []
  props.articles.forEach((article, index) => {
    const flower = createFlower(article, index)
    flowers.push(flower)
    scene.add(flower)
  })
}

const onMouseMove = (e) => {
  const rect = container.value.getBoundingClientRect()
  mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1
  mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1

  raycaster.setFromCamera(mouse, camera)
  const intersects = raycaster.intersectObjects(flowers, true)

  if (hoveredFlower && hoveredFlower !== intersects[0]?.object.parent) {
    hoveredFlower.scale.set(1, 1, 1)
    hoveredFlower = null
    container.value.style.cursor = 'default'
  }

  if (intersects.length > 0) {
    let obj = intersects[0].object
    while (obj.parent && !obj.userData.article) {
      obj = obj.parent
    }
    if (obj.userData.article && obj !== hoveredFlower) {
      hoveredFlower = obj
      hoveredFlower.scale.set(1.2, 1.2, 1.2)
      container.value.style.cursor = 'pointer'
    }
  }
}

const onClick = () => {
  if (hoveredFlower?.userData?.article) {
    router.push(`/articles/${hoveredFlower.userData.article.id}`)
  }
}

const onResize = () => {
  const w = container.value.clientWidth
  const h = container.value.clientHeight
  camera.aspect = w / h
  camera.updateProjectionMatrix()
  renderer.setSize(w, h)
}

const animate = () => {
  animationId = requestAnimationFrame(animate)

  const time = Date.now() * 0.001

  // Animate flowers - gentle swaying
  flowers.forEach(flower => {
    if (flower !== hoveredFlower) {
      // Gentle sway
      flower.rotation.z = Math.sin(time * flower.userData.rotationSpeed + flower.userData.phase) * 0.05
      flower.rotation.x = Math.sin(time * 0.5 + flower.userData.phase) * 0.02

      // Flower head bobbing
      if (flower.userData.flowerHead) {
        flower.userData.flowerHead.rotation.y = Math.sin(time * 0.3 + flower.userData.phase) * 0.1
      }
    }
  })

  // Camera orbit - slow rotation
  cameraAngle += 0.0005
  camera.position.x = Math.sin(cameraAngle) * 15
  camera.position.z = Math.cos(cameraAngle) * 15
  camera.lookAt(0, 2, 0)

  renderer.render(scene, camera)
}

watch(() => props.articles, (newArticles) => {
  if (scene && newArticles.length > 0) {
    createFlowers()
  }
})

onMounted(() => {
  initScene()
  animate()
  window.addEventListener('resize', onResize)
  container.value.addEventListener('mousemove', onMouseMove)
  container.value.addEventListener('click', onClick)
})

onUnmounted(() => {
  cancelAnimationFrame(animationId)
  window.removeEventListener('resize', onResize)
  if (renderer) renderer.dispose()
})
</script>

<style scoped>
.three-container {
  width: 100%;
  height: 100vh;
  overflow: hidden;
}
</style>