<template>
  <nav>
    <router-link to="/">Sign In</router-link> |
    <router-link to="/FirstPage">First Page</router-link> |
    <router-link to="/PP1Search">PP1 Search</router-link> |
    <router-link to="/PP3Detail">PP3 Detail</router-link> |
    <router-link to="/PP1Result">PP1 Result</router-link> |
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
