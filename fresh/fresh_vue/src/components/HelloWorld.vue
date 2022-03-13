<template>
  <div class="hello">
    <div v-for="(i,index) in msg" :key="index">
      <h1>
        {{i.name}}
      </h1>
    </div>


  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: []
    }
  },
  mounted() {
    this.a()
  },
  methods:{
    a(){
      this.$axios.get("/apis").then(res=>{
        this.msg = res.data
        if(res===1){
          console.log("ok")
        }
      }).catch(error=>{
        console.log("no")
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
