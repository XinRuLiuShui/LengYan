<template>
  <div class="chant-page">

    <!-- 左右导航 -->
    <div class="nav-left">
      <router-link to="/">首页</router-link>
    </div>
    <div class="nav-right" v-if="nextChant">
      <router-link :to="'/' + nextChant.path">下一篇</router-link>
    </div>

    <!-- 咒语内容 -->
    <div v-if="chant" class="chant-content">
      <h1>{{ chant.title }}</h1>

      <div v-for="(section, sIndex) in chant.sections" :key="sIndex">
        <h2>{{ section.title }}</h2>
        <div v-for="(item, index) in section.chants" :key="index" class="chant-block">
          <div class="pinyin">{{ item.pinyin }}</div>
          <div class="text">{{ item.text }}</div>
          <div class="meaning">{{ item.meaning }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import chants from '../data/chants.js'

const route = useRoute()
const chant = ref(null)
const nextChant = ref(null)

const loadChant = async (chapter) => {
  // 用 path 字段匹配，而不是 id
  const current = chants.find(c => c.path === chapter)
  if (!current) return

  const module = await import(`../data/${current.file}`)
  chant.value = module.default[0]

  // 下一篇也改用 path
  const nextItem = chants.find(c => c.id === current.id + 1)
  nextChant.value = nextItem || null
}

onMounted(async () => {
  loadChant(route.params.chapter)
})

watch(
  () => route.params.chapter,
  (newChapter) => loadChant(newChapter)
)
</script>

<style>
.chant-page {
  max-width: 900px;
  margin: auto;
  padding: 40px;
  position: relative;
}

.nav-left {
  position: fixed;
  top: 50%;
  left: 20px;
  transform: translateY(-50%);
}

.nav-right {
  position: fixed;
  top: 50%;
  right: 20px;
  transform: translateY(-50%);
}

.chant-block {
  margin-bottom: 30px;
}

.text {
  font-size: 22px;
  line-height: 1.8;
}

.pinyin {
  color: gray;
  margin-top: 6px;
}

.meaning {
  color: #666;
  margin-top: 6px;
  font-size: 15px;
}
</style>