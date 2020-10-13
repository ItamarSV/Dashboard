<template>
  <div>
    <b-alert
      id="myAlert"
      :show="dismissCountDown"
      dismissible
      variant="warning"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
      fade
    >
      This alert will dismiss after 5 seconds...
    </b-alert>
    <b-button @click="showAlert" variant="info" class="m-1">
      Show alert with count-down timer
    </b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      dismissSecs: 5,
      dismissCountDown: 0,
    };
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
  },
};

</script>
