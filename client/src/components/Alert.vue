<template>
  <div>
    <b-alert
      variant="success"
      show dismissible fade>{{ message }}</b-alert>
    <br>
  </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>

<style scoped>

</style>
