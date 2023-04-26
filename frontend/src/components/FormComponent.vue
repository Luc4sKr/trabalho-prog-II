<template>
    <div class="modal book-modal">
        <form id="book-form" @submit.prevent="include_book" method="post">
            <div class="form-control">
                <label for="title">Title</label>
                <input id="title-input" name="title" type="text" v-model="book.title">
            </div>
            <div class="form-control">
                <label for="category">Category</label>
                <select id="category-input" name="category" v-model="book.category_id">
                    <option v-for="category in categories" :key="category.id" v-bind:value="category.id">
                        {{ category.category_name }}
                    </option>
                </select>
            </div>
            <div class="form-control">
                <label for="author">Author</label>
                <input id="author-input" name="author" type="text" v-model="book.author">
            </div>
            <div class="form-control">
                <label for="grade">Grade: <span>{{ book.grade }}</span></label>
                <input id="grade-input" name="grade" type="range" min="0" max="5" v-model="book.grade">
            </div>
            <div class="form-control">
                <label for="resume">Resume</label>
                <textarea name="resume" id="resume" cols="30" rows="10" v-model="book.resume"></textarea>
            </div>
            <div class="form-control">
                <label for="reading-time">Reading Time</label>
                <div class="reading-time-input-container">
                    <input id="reading-time-input" name="reading-time" type="number" v-model="book.reading_time">
                    <span>Hours</span>
                </div>
            </div>

            <div class="buttons">
                <button id="btn-register" class="btn">Register</button>
            </div>
        </form>
    </div>
</template>

<script>
import api from "@/services/api.js";
import { ref } from 'vue';

export default {
    name: "FormComponent",
    data() {
        return {
            categories: [],

            book: {
                title: ref(""),
                author: ref(""),
                grade: ref(0),
                resume: ref(""),
                reading_time: ref(0),
                category_id: ref(1)
            }
        }
    },
    created() {
        this.fetch_categories()
    },
    methods: {
        fetch_categories: function () {
            api.get("/list/category")
                .then((response) => {
                    this.categories = response.data.category;
                })
                .catch((error) => {
                    console.log(error);
                });
        },
        include_book: function () {
            api.post("/include/book", this.book)
                .then((response) => {
                    console.log(response)
                }).catch((error) => {
                    console.log(error)
                });

            this.$emit("reload_books", this.book);
        }
    }
}
</script>

<style scoped>
.book-modal {
    width: 400px;
    height: 480px;
    background-color: #1D3461;
}

#book-form {
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.form-control {
    margin: 10px 0px 10px 0px;
    width: 220px;

    display: flex;
    flex-direction: column;
}

.form-control>label {
    color: #fff;
    font-weight: bold;
}

.form-control>input,
select {
    width: 220px;
}

.form-control>textarea {
    max-height: 80px;
    max-width: 220px;
    min-width: 220px;
}

.reading-time-input-container {
    color: #fff;
    width: 100%;
    float: left;
}

.reading-time-input-container>input {
    width: 30px;
    text-align: center;
    margin-right: 5px;
}

input[type=number]::-webkit-inner-spin-button {
    -webkit-appearance: none;

}

input[type=number] {
    -moz-appearance: textfield;
    appearance: textfield;
}

#btn-register {
    width: 100px;
}
</style>