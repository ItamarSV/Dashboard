<template>
  <div class="container">
    <div>
      <b-table hover :items="testdata"></b-table>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      testdata: [],
    };
  },

  methods: {
    gettestdata() {
      // const path = window.location.href.concat('/books');
      const path = 'http://localhost:5000/main';
      axios.get(path)
        .then((res) => {
          this.testdata = res.data.testdata;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },

  created() {
    this.gettestdata();
  },
};
</script>
