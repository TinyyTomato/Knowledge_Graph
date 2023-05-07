<template>
  <el-container class="show">
      <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="默认" name="first">
        <el-table
          height="700"
          :data="quoteData"
          style="width: 100%">
          <el-table-column
            prop="title"
            label="标题"
            width="180">
          </el-table-column>
          <el-table-column
            prop="author"
            label="作者"
            width="180">
          </el-table-column>
          <el-table-column
            prop="n_citation"
            label="引用次数"
            width="80">
          </el-table-column>
          <el-table-column
            prop="raw"
            label="期刊"
            width="80">
          </el-table-column>
          <el-table-column
            prop="year"
            label="年份"
            width="60">
          </el-table-column>
          <el-table-column
            prop="url"
            label="链接"
            width="180">
          </el-table-column>
          <el-table-column
            prop="abstract"
            label="摘要"
            width="500">
          </el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="发表时间" name="second">
        <el-table
          height="700"
          :data="tableData"
          style="width: 100%">
          <el-table-column
            prop="abstract"
            label="摘要"
            width="300">
          </el-table-column>
          <el-table-column
            prop="title"
            label="标题"
            width="180">
          </el-table-column>
          <el-table-column
            prop="author"
            label="作者"
            width="180">
          </el-table-column>

        </el-table>
      </el-tab-pane>
      <el-tab-pane label="访问量" name="third"></el-tab-pane>
      <el-tab-pane label="引用次数" name="fourth">
        <el-table
          height="700"
          :data="n_Data"
          style="width: 100%">
          <el-table-column
            prop="title"
            label="标题"
            width="180">
          </el-table-column>
          <el-table-column
            prop="author"
            label="作者"
            width="180">
          </el-table-column>
          <el-table-column
            prop="n_citation"
            label="引用次数"
            width="80">
          </el-table-column>
          <el-table-column
            prop="raw"
            label="期刊"
            width="80">
          </el-table-column>
          <el-table-column
            prop="year"
            label="年份"
            width="60">
          </el-table-column>
          <el-table-column
            prop="url"
            label="链接"
            width="180">
          </el-table-column>
          <el-table-column
            prop="abstract"
            label="摘要"
            width="180">
          </el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="会议/期刊" name="fifth">会议/期刊</el-tab-pane>
      <el-tab-pane label="h指数" name="sixth">h指数</el-tab-pane>
    </el-tabs>
    <el-container class="graph">
        <el-main>
          <echart1></echart1>
        </el-main>
    </el-container>
  </el-container>

</template>

<script>
    import echart1 from "./community.vue";
    import list2 from "../../../static/person2paper.json"
    import list4 from "../../../static/PersonPaper.json"
    import listn from "../../../static/PersonPaper_n.json"
    export default {
        name: "profile",
      components: {echart1},
      data () {
        return {
          radio: '1',
          tableData: [],
          quoteData: [],
          n_Data: [],
          list2: list2,
          list4: list4,
          link4: [],
          listn: listn
        };
      },
      methods: {
        handleClick(tab, event) {
          // let data = {}
          for (let i = 0; i < this.list2.hits.hits.length; i++) {
            let data2 = {}
            data2.title = this.list2.hits.hits[i]._source.document.title
            data2.author = this.list2.hits.hits[i]._source.document.authors.map(v => v.name).join(',')
            data2.abstract = this.list2.hits.hits[i]._source.document.abstract
            // console.log(this.tableData.author)
            this.tableData.push(data2)
          }
          for (let i = 0; i < this.list4.quote.length; i++) {
            let data4 = {}
            data4.title = this.list4.quote[i].title
            data4.author = this.list4.quote[i].authors.map(v => v.name).join(',')
            data4.n_citation = this.list4.quote[i].n_citation
            data4.raw = this.list4.quote[i].raw
            data4.year = this.list4.quote[i].year
            data4.url = this.list4.quote[i].url
            let link4=[];
            link4 = data4.url
            //data4.abstract = this.list4.quote[i].abstract
            // console.log(this.quoteData.author)
            this.quoteData.push(data4)
          }
          for (let j = 0; j < this.listn.n.length; j++) {
            let datan = {}
            datan.title = this.listn.n[j].title
            datan.author = this.listn.n[j].authors.map(v => v.name).join(',')
            datan.n_citation = this.listn.n[j].n_citation
            datan.raw = this.listn.n[j].raw
            datan.year = this.listn.n[j].year
            datan.url = this.listn.n[j].url

            datan.abstract = this.listn.n[j].abstract
            // console.log(this.quoteData.author)
            this.n_Data.push(datan)
          }
        }
      }
    }
</script>

<style scoped>
  .el-main {
    background-color: #f9fafc;
    text-align: center;
    line-height: 500px;
    justify-content: space-between;
    font-size: smaller;
    height: 100%;
  }

  .show{
    height: 100vh;

  }

  .graph{
    height: 100%;

  }

  .el-tabs{
    width: 800px;
    margin-right: 30px;
    margin-left: 30px;
    color: #ffffff;
  }
  .el-tab-pane{
    color: #895454;
  }
  body > .el-container {
    margin-bottom: 50px;
  }
</style>
