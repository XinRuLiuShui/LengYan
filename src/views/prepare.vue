<template>
  <div class="chant-page">

    <!-- 左右导航 -->
    <div class="nav-left">
      <router-link to="/">首页</router-link>
    </div>
    <div class="nav-right">
      <router-link to="/chapter1">下一篇</router-link>
    </div>

    <!-- 内容 -->
    <div class="chant-content">
      <h1>请法</h1>
      <div v-for="(block, index) in texts" :key="index" class="chant-block">
        <div class="text">{{ block }}</div>
      </div>
    </div>

  </div>
</template>

<script setup>
// 这里直接用数组存储内容，和你之前 JSON 的风格统一
const texts = [
  "大佛顶如来密因修证了义诸菩萨万行首楞严经",

  "南无本师释迦牟尼佛!\n南无本师释迦牟尼佛!\n南无本师释迦牟尼佛!",

  "南无楞严会上佛菩薩!\n南无楞严会上佛菩薩!\n南无楞严会上佛菩薩!",

  
"妙湛总持不动尊，\n首楞严王世希有。\n销我亿劫颠倒想，\n不历僧祇获法身。\n愿今得果成宝王，\n还度如是恒沙众。\n将此深心奉尘刹，\n是则名为报佛恩。\n伏请世尊为证明，\n五浊恶世誓先入。\n如一众生未成佛，\n终不于此取泥洹。\n大雄大力大慈悲，\n希更审除微细惑。\n令我早登无上觉，\n于十方界坐道场。\n舜若多性可销亡，\n烁迦罗心无动转。",
"南无常住十方佛。\n南无常住十方法。\n南无常住十方僧。\n南无释迦牟尼佛。\n南无佛顶首楞严。\n南无观世音菩薩。\n南无金刚藏菩薩。",



  `尔时世尊，从肉髻中，涌百宝光。光中涌出，千叶宝莲。有化如来，坐宝华中。顶放十道，百宝光明。
一一光明，皆遍示现，十恒河沙，金刚密迹，擎山持杵， 遍虚空界。大众仰观，畏爱兼抱。求佛哀祐，
一心听佛，无见顶相，放光如来，宣说神咒。`
]
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
  white-space: pre-wrap;
}
</style>