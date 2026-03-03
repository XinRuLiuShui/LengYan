<template>
  <div class="home">
    <h1>楞严咒</h1>
    <ul>
      <li v-for="c in chants" :key="c.id">
        <router-link :to="'/' + c.path">{{ c.title }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script setup>
import chants from '../data/chants.js'
</script>

<style>
.home {
  text-align: center;
  margin-top: 100px;
}
ul {
  list-style: none;
  padding: 0;
}
li {
  margin: 20px 0;
  font-size: 22px;
}
</style>