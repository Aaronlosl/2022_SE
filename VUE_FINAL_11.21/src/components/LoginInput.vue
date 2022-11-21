<template>
  <div class="Login input">
    <el-input placeholder="less than 25 chars" v-model="username" clearable>
    </el-input>
    <el-input placeholder="less than 25 chars" v-model="password" show-password clearable>
    </el-input>
  </div>
</template>


<script>
export default {
  name: 'LoginInput',
  data() {
    return {
      username: '',
      password: ''
    }
  }
}
</script>