<template>
  <div
    id="knowledgeGraph"
    :style="{
          // marginLeft:'180px',
          height: '100%',
          width: '100%',
        }"
  ></div>
</template>
<script>
  import axios from "axios";
  import Vnodes from "../../../static/node_socre.json"
  import Vlinks from "../../../static/my_edge.json"
  let knowledgeGraph = "";
  import * as echarts from "echarts";
  export default {
    name: "echart1",
    data() {
      return {
        Vnode: Vnodes,
        Vlink: Vlinks,
      };
    },
    mounted() {
      this.getData();
      this.draw();
    },
    methods: {
      getData() {
        axios.get('../../../static/paper2person.json').then(response => {
          console.log(response.data);
        }, response => {
          console.log("error");
        });
      },
      draw() {
        let that = this;
        this.knowledgeGraphVision = true;
        this.$nextTick(() => {
          knowledgeGraph = echarts.init(
            document.getElementById("knowledgeGraph")
          );
          let categories = [];
          let data = [];
          for (let i = 0; i < that.Vnode.length; i++) {
            data[i] = {
              name: that.Vnode[i].name,
              x: Math.random() * 500 + 200,
              y: Math.random() * 500 + 200,
              symbolSize: that.Vnode[i].value * 5 + 10,
              value: that.Vnode[i].name
            };
          }
          let graph = { nodes: data };
          graph.nodes.forEach(function (node) {
            // node.category = node.class;
            node.draggable = true;
          });
          let options = {
            legend: [
              {
                // selectedMode: 'single',
                data: categories.map(function (a) {
                  return a.name;
                }),
              },
            ],
            series: [
              {
                type: "graph",
                layout: "force",
                data: data,
                links: that.Vlink,

                // edgeSymbol: ["circle"],
                width: "90%",
                height: "100%",
                roam: false,
                edgeLabel: {
                  normal: {
                    show: false,
                    formatter: function (x) {
                      return x.data.name;
                    },
                  },
                },
                label: {
                  show: true,
                },
                force: {
                  repulsion: 100,
                },
                lineStyle: {
                  width: 1.5,
                },
              },
            ],
          };
          knowledgeGraph.setOption(options);
        });
      },
    },
  }

</script>
<style scoped>

</style>
