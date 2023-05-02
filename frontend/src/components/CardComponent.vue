<template>
    <div class="card">
        <div class="card-head">
            <h3 class="title">{{ title }}</h3>
        </div>
        <div class="card-body">
            <div class="infos">
                <span><strong>Category: </strong>{{ category.category_name }}</span>
                <span><strong>Author: </strong>{{ author }}</span>
                <span><strong>Grade: </strong> {{ grade }}</span>
                <span><strong>Reading Time: </strong>{{ reading_time }}</span>
            </div>
            <div class="resume-container">
                <p class="resume"><strong>Resume: </strong>{{ resume }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "CardComponent",
    props: {
        id: {
            type: Number,
            required: true
        },
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
    },
    data() {
        return {

        }
    },
    methods: {
        
    }
}
</script>

<style scoped>
.card {
    width: 320px;
    height: 200px;
    padding: 10px;
    box-shadow: 2px 2px 15px #1D3461;
    background-color: #fff;

    cursor: pointer;
}

.card-head {
    padding: 10px;
}

.title {
    text-align: center;
}

.card-body {
    display: block;
}

.infos {
    display: flex;
    flex-direction: column;
}

.resume-container {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>