// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

import Vue from 'vue'//引入vue.js文件
import App from './App'//引入当前目录下的App.vue文件，【./】指当前目录，【.vue】被隐藏了
import router from './router'//自动扫描里面的路由配置
import JsonViewer from 'vue-json-viewer'
Vue.use(JsonViewer)
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import * as echarts from 'echarts'

Vue.config.productionTip = false//屏蔽调试时的一些console日志内容
Vue.prototype.$echarts = echarts

/* eslint-disable no-new */
new Vue({
  el: '#app',
  //配置路由
  router,
  components: { App },
  template: '<App/>'
});
