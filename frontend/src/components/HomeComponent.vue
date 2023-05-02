<template>
    <HeaderComponent />
    <div class="wrapper">
        <div class="modal-container">
            <button id="btn-modal" class="btn" @click="toggle_form_modal">{{ btn_modal_txt }}</button>
            <Teleport to="#modal">
                <FormComponent v-if="form_open" />
            </Teleport>
        </div>

        <div id="books-list" class="grid-container">
            <div class="grid-item" v-for="book in books" :key="book.id">
                <CardComponent v-bind="book" @click="open_card_modal(book.id)" />
            </div>
            <div v-if="books.length <= 0">
                <h2 class="msg-not-found">No registered book</h2>
            </div>
        </div>

        <div class="card-modal-container">
            <Teleport to="#modal">
                <div v-if="card_modal_open" class="modal card-book-modal">
                    <CardComponent v-bind="book_modal" />
                    <div class="btn-container">
                        <button class="btn close-btn-card-modal" @click="close_card_modal">Close</button>
                    </div>
                </div>
            </Teleport>
        </div>
    </div>
</template>

<script>
import HeaderComponent from './HeaderComponent.vue';
import FormComponent from './FormComponent.vue';
import CardComponent from './CardComponent.vue';

import api from "@/services/api.js";

export default {
    name: "HomeComponent",
    components: {
        HeaderComponent,
        FormComponent,
        CardComponent
    },
    data() {
        return {
            form_open: false,
            btn_modal_txt: "Open Form",
            books: [],

            card_modal_open: false,
            book_modal: {}
        }
    },
    created() {
        this.fetch_books();
    },
    methods: {
        toggle_form_modal: function () {
            if (this.card_modal_open) {
                return
            }

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
        },
        open_card_modal: async function (id) {
            try {
                const response = await api.get(`/list/book/${id}`);
                console.log(response.data.book);
                this.book_modal = response.data.book;
            } catch (error) {
                console.log(error);
            }

            this.card_modal_open = true;
        },
        close_card_modal: function() {
            this.card_modal_open = false;
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

.card-book-modal {
    width: 320px;
    min-height: 300px;
    padding: 10px;
    background-color: #fff;
    box-shadow: 2px 2px 15px #1D3461;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.card-book-modal .card {
    box-shadow: none;
    width: auto;
    height: auto;
    padding: 0px;
}

.card-book-modal .btn-container {
    display: flex;
    justify-content: center;
    align-items: center;
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
    width: auto;
    height: auto;
    margin: 10px;
    margin-bottom: 30px;
    border-radius: 6px;
}

.msg-not-found {
    font-size: 28px;
    text-align: center;
}
</style>