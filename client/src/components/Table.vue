<template>
  <div class="container">
    <div>
      <b-table hover :items="testdata"></b-table>
      <b-spinner label="Spinning" v-if=!finishloading></b-spinner>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Vue from 'vue';

export default {
  data() {
    return {
      testdata: [],
      finishloading: false,
    };
  },

  methods: {
    gettestdata() {
      // const path = window.location.href.concat('/books');
      const path = 'http://localhost:5000/main';
      axios.get(path)
        .then((res) => {
          this.testdata = res.data.testdata;
          Vue.nextTick(this.finish());
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    finish() {
      this.finishloading = true;
    },
  },
  mounted() {
    this.gettestdata();
    // this.nextTick(function after() {
    //   this.finishloading = true;
    // });
  },
  // mounted() {
  // },
};
</script>
