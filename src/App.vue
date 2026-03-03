<script setup>
//import HelloWorld from './components/HelloWorld.vue'
// import { ref } from "vue"

// const showPinyin = ref(true)

// const text = [
//   { char: "南", pinyin: "ná" },
//   { char: "无", pinyin: "mó" },
//   { char: "楞", pinyin: "léng" },
//   { char: "严", pinyin: "yán" },
//   { char: "咒", pinyin: "zhòu" }
// ]

//import chant from "./chapter2.json"
</script>

<template>
  <!-- <div>
    <a href="https://vite.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" /> -->

  <!-- <div class="container">
    <button @click="showPinyin = !showPinyin">
      切换拼音
    </button>

    <div class="chant">
      <span v-for="(item, index) in text" :key="index">
        <ruby>
          {{ item.char }}
          <rt v-if="showPinyin">{{ item.pinyin }}</rt>
        </ruby>
      </span>
    </div>
  </div> -->

  <!-- <div class="container">

    <div v-for="(chapter, cIndex) in chant" :key="cIndex">
      <h1>{{ chapter.title }}</h1>

      <div v-for="(section, sIndex) in chapter.sections" :key="sIndex">
        <h2>{{ section.title }}</h2>

        <div v-for="(item, index) in section.chants" :key="index" class="chant-block">
          <div class="pinyin">{{ item.pinyin }}</div>
          <div class="text">{{ item.text }}</div>
          
          <div class="meaning">{{ item.meaning }}</div>
        </div>

      </div>
    </div>

  </div> -->
  <router-view />
</template>

<!-- <style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style> -->
<!-- 
<style>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.container {
  text-align: center;
}

.chant {
  font-size: 35px;   /* 主体文字大小 */
  line-height: 1.8;  /* 行间距 */
}

.chant ruby {
  ruby-position: over;    /* 确保拼音在汉字上方 */
}

.chant rt {
  padding-bottom: 8px;   /* 调整上下距离 */
}
</style> -->

<style>
.container {
  max-width: 900px;
  margin: auto;
  padding: 40px;
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