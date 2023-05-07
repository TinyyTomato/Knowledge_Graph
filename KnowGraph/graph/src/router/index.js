import Vue from 'vue'
import VueRouter from 'vue-router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

import main from '../views/Main'
import profile from '../views/user/profile'
//安装路由
Vue.use(VueRouter)
Vue.use(ElementUI)

//配置导出路由
export default new VueRouter({
  mode: 'history',  //去掉url中的#
  routes: [
    {
      //路由路径
      path: '/',
      name: 'main',
      //跳转的组件
      component: main,
      children:[
        {
          path: '/user/profile',
          component:profile
        }
      ]
    }
  ]
});
