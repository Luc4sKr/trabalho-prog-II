<template>
    <HeaderComponent />
    <div class="wrapper">
        <div class="modal-container">
            <button id="btn-modal" class="btn" @click="toggle_modal">{{ btn_modal_txt }}</button>
            <Teleport to="#modal">
                <FormComponent v-if="modal_open" @reload_books="reload"/>
            </Teleport>
        </div>

        <!-- Listagem -->
        <div id="books-list" class="grid-container">
            <div v-if="books.length > 0">
                <div class="grid-item" v-for="book in books" :key="book.id">
                    <div class="card">
                        <div class="title">
                            <h2>{{ book.title }}</h2>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else>
                <h2 class="msg-not-found">No registered book</h2>
            </div>
        </div>
    </div>
</template>

<script>
import HeaderComponent from './HeaderComponent.vue';
import FormComponent from './FormComponent.vue';
import api from "@/services/api.js";

export default {
    name: "HomeComponent",
    components: {
        HeaderComponent,
        FormComponent
    },
    data() {
        return {
            modal_open: false,
            btn_modal_txt: "Open Form",
            books: []
        }
    },
    created() {
        this.fetch_books();
    },
    methods: {
        toggle_modal: function () {
            this.modal_open = !this.modal_open;
            this.btn_modal_txt = this.modal_open ? "Close Form" : "Open Form";
        },
        fetch_books: function () {
            api.get("/list/book")
                .then((response) => {
                    this.books = response.data.book;
                }).catch((error) => {
                    console.log(error)
                });
            
            console.log(this.books)
        },
        reload: function () {
            api.get("/list/book")
                .then((response) => {
                    this.books = response.data.book;
                });
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
    border: 1px solid #000;
    border-radius: 6px;
}

.msg-not-found {
    font-size: 28px;
    text-align: center;
}
</style>