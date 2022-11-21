<template>
  <div class="fixedSearch" v-show="showFixedSearch">
    <searchBtn class="searchBtn" href="https://" target="_blank" rel="noopener">
      <img src="@/assets/箭头二.svg">
    </searchBtn>
    <textarea class="helping information input box" maxlength="50" placeholder="less than 50 chars" cols="32"
      style="resize:none;" v-model="searchBox">
          </textarea>
    <searchBtn href="https://" target="_blank" rel="noopener">
      <img src="@/assets/search.svg">
    </searchBtn>
  </div>
</template>
  
  
<script>
export default {
  name: 'SearchAndBack',
  data() {
    return {
      searchInfo: ''
    }
  }
}
</script>