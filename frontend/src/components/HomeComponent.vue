<template>
    <HeaderComponent />
    <div class="wrapper">
        <div class="modal-container">
            <button id="btn-modal" class="btn" @click="toggle_modal">{{ btn_modal_txt }}</button>
            <Teleport to="#modal">
                <FormComponent v-if="form_open" />
            </Teleport>
        </div>

        <div id="books-list" class="grid-container">
            <div class="grid-item" v-for="book in books" :key="book.id">
                <BookCardComponent v-bind="book"/>
            </div>
            <div v-if="books.length <= 0">
                <h2 class="msg-not-found">No registered book</h2>
            </div>
        </div>
    </div>
</template>

<script>
import HeaderComponent from './HeaderComponent.vue';
import FormComponent from './FormComponent.vue';
import BookCardComponent from './BookCardComponent.vue';
import api from "@/services/api.js";

export default {
    name: "HomeComponent",
    components: {
        HeaderComponent,
        FormComponent,
        BookCardComponent
    },
    data() {
        return {
            form_open: false,
            btn_modal_txt: "Open Form",
            books: []
        }
    },
    created() {
        this.fetch_books();
    },
    methods: {
        toggle_modal: function () {
            this.form_open = !this.form_open;
            this.btn_modal_txt = this.form_open ? "Close Form" : "Open Form";
        },
        fetch_books: function () {
            api.get("/list/book")
                .then((response) => {
                    this.books = response.data.book;
                }).catch((error) => {
                    console.log(error)
                });

            console.log(this.books)
        }
    }
}
</script>

<style scoped>
.wrapper {
    width: 80%;
    margin: 0 auto;
}

.modal-container {
    width: 100%;
}

#btn-modal {
    width: 100px;
    height: auto;
    margin: 10px;
}

.grid-container {
    display: grid;
    place-items: center;
    grid-template-columns: auto auto auto;
    padding: 10px;
}

.grid-item {
    background-color: #fff;
    width: 300px;
    height: 210px;
    margin: 10px;
    margin-bottom: 30px;
    border-radius: 6px;
}

.msg-not-found {
    font-size: 28px;
    text-align: center;
}
</style>