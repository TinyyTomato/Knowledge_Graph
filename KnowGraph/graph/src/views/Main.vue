<template>
  <div class="header">
    <Header></Header>
    <profile></profile>
    <router-view></router-view>
  </div>
</template>


<script>
  import Header from './user/Header'
  import profile from './user/profile'
  export default {
    components: {
      Header,
      profile,
    },
    name: "main",
    data() {
      return {
        input1: '',
        input2: '',
        input3: '',
        select: ''
      }
    }
  }

</script>

<style scoped>
  .header {
    position: absolute;
    line-height: 50px;
    top: 0px;
    left: 0px;
    right: 0px;
    background-color: #7c97bb;
  }
  .el-select .el-input {
    width: 130px;
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }
</style>
