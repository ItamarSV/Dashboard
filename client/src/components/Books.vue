<template>
  <div class="container">
    <div>
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="#">NavBar</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item href="#">Link</b-nav-item>
            <b-nav-item href="#" disabled>Disabled</b-nav-item>
          </b-navbar-nav>

          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <b-nav-form>
              <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
              <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
            </b-nav-form>

            <b-nav-item-dropdown text="Lang" right>
              <b-dropdown-item href="#">EN</b-dropdown-item>
              <b-dropdown-item href="#">ES</b-dropdown-item>
              <b-dropdown-item href="#">RU</b-dropdown-item>
              <b-dropdown-item href="#">FA</b-dropdown-item>
            </b-nav-item-dropdown>

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
    <div class="">
      <div class="">
        <h1>Books</h1>
        <hr><br><br>
        <b-alert
          id="myAlert"
          :show="dismissCountDown"
          dismissible
          :variant="alertVariant"
          @dismissed="dismissCountDown=0"
          @dismiss-count-down="countDownChanged"
          fade
        >{{ message }}
        </b-alert>
        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.book-modal>Add Book</button>
        <br><br>
      </div>
    </div>
    <button
        type="button"
        class="btn btn-primary mt-5"
        v-b-modal.book-table>Insert book list to DB</button>
    <b-modal ref="bookTable"
             id="book-table"
             title="List of Books on the system"
             size="xl"
             hide-footer>
      <b-form class="w-400">
        <div>
          <b-table striped hover :items="books"></b-table>
        </div>
        <b-button class="btn btn-primary mt-5 w-25" @click=hideTable>Close Me</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="addBookModal"
             id="book-modal"
             title="Add a new book"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="Title:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addBookForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Author:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addBookForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button @click="showAlert" type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editBookModal"
             id="book-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Title:"
                    label-for="form-title-edit-input">
          <b-form-input id="form-title-edit-input"
                        type="text"
                        v-model="editForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-edit-group"
                      label="Author:"
                      label-for="form-author-edit-input">
            <b-form-input id="form-author-edit-input"
                          type="text"
                          v-model="editForm.author"
                          required
                          placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-edit-group">
          <b-form-checkbox-group v-model="editForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button @click="showAlert" type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="deleteBookModal"
             id="book-delete-modal"
             title="Delete Book"
             hide-footer>
      <b-form @submit="onSubmitDelete" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-title-edit-group"
                    label="Are you sure that you what to delete this book?"
                    label-for="form-title-edit-input">
        </b-form-group>
        <b-button-group class="position-flex justify-content-between flex-row">
          <b-button
            class="position-flex justify-content-between"
            @click="showAlert" type="submit" variant="primary">Delete</b-button>
          <b-button
            class="position-flex justify-content-between"
            type="reset"
            variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
// import * as d3 from 'd3';

export default {
  data() {
    return {
      books: [],
      addBookForm: {
        title: '',
        author: '',
        read: [],
        id: '',
        price: '',
      },
      message: '',
      showMessage: false,
      editForm: {
        uuid: '',
        title: '',
        author: '',
        read: [],
        id: '',
        price: '',
      },
      removeForm: {
        uuid: '',
        title: '',
        author: '',
        read: [],
        id: '',
        price: '',
      },
      dismissSecs: 5,
      dismissCountDown: 0,
      alertVariant: 'warning',
    };
  },
  watch: {
  },
  components: {
    // alert: Alert,
    // alerts: Alerts,
  },
  mounted() {
    // Alerts.showAlert();
  },

  methods: {
    getBooks() {
      // const path = window.location.href.concat('/books');
      const path = 'http://localhost:5000/books';
      axios.get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addBook(payload) {
      // const path = window.location.href.concat('/books');
      const path = 'http://localhost:5000/books';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book added!';
          this.showMessage = true;
          this.alertVariant = 'success';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getBooks();
        });
    },
    updateBook(payload, bookID) {
      // const path = window.location.href.concat(`/books/${bookID}`);
      const path = `http://localhost:5000/books${bookID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Book updated!';
          this.showMessage = true;
          this.alertVariant = 'success';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    removeBook(bookID) {
      // const path = window.location.href.concat(`/books/${bookID}`);
      const path = `http://localhost:5000/books${bookID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Book removed!';
          this.showMessage = true;
          this.alertVariant = 'success';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getBooks();
        });
    },
    onDeleteBook(book) {
      this.removeBook(book.uuid);
    },
    initForm() {
      this.addBookForm.title = '';
      this.addBookForm.author = '';
      this.addBookForm.read = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.author = '';
      this.editForm.read = [];
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      let read = false;
      if (this.addBookForm.read[0]) read = true;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addBookModal.hide();
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      let read = false;
      if (this.editForm.read[0]) read = true;
      const payload = {
        title: this.editForm.title,
        author: this.editForm.author,
        read,
      };
      this.updateBook(payload, this.editForm.uuid);
    },
    onSubmitDelete(evt) {
      evt.preventDefault();
      this.$refs.deleteBookModal.hide();
      // let read = false;
      // if (this.removeForm.read[0]) read = true;
      // const payload = {
      //   title: this.removeForm.title,
      //   author: this.removeForm.author,
      //   read,
      // };
      this.removeBook(this.removeForm.uuid);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editBookModal.hide();
      this.initForm();
      this.getBooks(); // why?
    },
    onResetDelete(evt) {
      evt.preventDefault();
      this.$refs.deleteBookModal.hide();
      // this.initForm();
      // this.getBooks(); // why?
    },
    editBook(book) {
      this.editForm = book;
    },
    removeBookModel(book) {
      this.removeForm = book;
    },
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
    hideTable() {
      this.$refs.bookTable.hide();
    },

  },

  created() {
    this.getBooks();
  },
  editBook(book) {
    this.editForm = book;
  },
  deleteBook(book) {
    this.editForm = book;
  },

};
</script>
