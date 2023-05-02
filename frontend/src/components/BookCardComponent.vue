<template>
    <div class="card">
        <div class="title">
            <h2>{{ title }}</h2>
        </div>
        <div class="body">
            <p><strong>Category</strong>: {{ category.category_name }}</p>
            <p><strong>Author</strong>: {{ author }}</p>
            <p><strong>Grade</strong>: {{ grade }}</p>
            <p><strong>Reading</strong> Time: {{ reading_time }}</p>
            <p class="resume"><strong>Resume</strong>: {{ resume }}</p>
        </div>
    </div>
</template>

<script>
export default {
    name: "BookCardComponent",
    data() {
        return {

        }
    },
    props: {
        title: {
            type: String,
            required: true
        },
        category: {
            type: Object,
            required: true
        },
        author: {
            type: String,
            required: true
        },
        grade: {
            type: Number,
            required: true
        },
        reading_time: {
            type: Number,
            required: true
        },
        resume: {
            type: String,
            required: true
        }
    }
}
</script>

<style scoped>
.card {
    width: 100%;
    height: 100%;
    padding: 10px;
    box-shadow: 1px 1px 2px #000;

    cursor: pointer;
}

.title {
    width: 100%;
    min-height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
}

.title>h2 {
    text-align: center;
}

.resume {
    display: -webkit-box;
    -webkit-line-clamp: 4;
    overflow: hidden;
    -webkit-box-orient: vertical;
}
</style>