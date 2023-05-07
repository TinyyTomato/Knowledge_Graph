<template>
  <div style="margin-top: 15px;">
    <h1>你的智能查询助手</h1>
    <el-input placeholder="请输入内容" v-model="input3" class="input-with-select">
      <el-select v-model="select" slot="prepend" placeholder="请选择">
        <el-option label="查作者" value="1"></el-option>
        <el-option label="查论文" value="2"></el-option>
      </el-select>
      <el-button slot="append" icon="el-icon-search"></el-button>
    </el-input>
  </div>
</template>

<script>
    export default {
        name: "Header",
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
  .el-select .el-input {
    width: 400px;
    text-align: left;
  }
  .el-button{
    border-left-width: 30px;
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }

</style>
