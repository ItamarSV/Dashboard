<template>
  <div class="container">
    <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">NavBar</b-navbar-brand>

        <!-- <b-navbar-toggle target="nav-collapse"></b-navbar-toggle> -->

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class=" mt-1" pills>
            <b-nav-item class="mr-2" @click="Activenav('Home')" Active>Home</b-nav-item>
            <b-nav-item class="mr-2" @click="Activenav('Data Analysis')">Data Analysis</b-nav-item>
            <b-nav-item class="mr-2" @click="Activenav('Active')">Active</b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <!-- <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form> -->

            <!-- <b-nav-item-dropdown text="Lang" right>
              <b-dropdown-item href="#">EN</b-dropdown-item>
              <b-dropdown-item href="#">ES</b-dropdown-item>
              <b-dropdown-item href="#">RU</b-dropdown-item>
              <b-dropdown-item href="#">FA</b-dropdown-item>
            </b-nav-item-dropdown> -->

            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <em>User</em>
              </template>
              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item href="#">Sign Out</b-dropdown-item>
            </b-nav-item-dropdown>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
    <button type="button" class="btn btn-primary">Main check</button>
    <b-avatar icon="star-fill" size="4em"></b-avatar>
    <b-avatar src="https://placekitten.com/300/300"></b-avatar>
    <b-avatar src="dist/WebAvatar.jpg" size="6rem"></b-avatar>
    <b-overlay :show="show" rounded="sm">
      <itamartable v-if="activeNav==='Home'"></itamartable>
    </b-overlay>
  </div>
</template>

<script>
// import axios from 'axios';
import Table from './Table.vue';

export default {
  data() {
    return {
      activeNav: 'Home',
      show: true,
    };
  },

  components: {
    itamartable: Table,
  },

  methods: {
    Activenav(nav) {
      this.activeNav = nav;
    },
  },

  created() {
  },
};
</script>
<style scoped>
.nav-pills .nav-link.active, .nav-pills .show>.nav-link {
  background-color: transparent;
  border-radius: 0rem;
}
.navbar-dark .navbar-nav .nav-link {
    color: rgba(255, 255, 255);
    border-bottom-style: solid;
    border-color: transparent;
}
.navbar-dark .navbar-nav .nav-link:hover,
.navbar-dark .navbar-nav .nav-link:focus,
.navbar-dark .navbar-nav .nav-link:active{
  color: rgba(255, 255, 255);
  border-bottom-color: white !important;
}
a.nav-link {
  color: white;
}
</style>
