<template>
    <div v-for="minion in minions" :key="minion.id">
        <h1>{{ minion.name }}</h1>
        <MinionComponent v-bind="minion"/>
    </div>

    
</template>

<script>
import MinionComponent from './minion/MinionComponent.vue';

import api from '@/services/api';

export default {
    name: "MinionListComponent",
    data() {
        return {
            minions: []
        }
    },
    components: {
        MinionComponent
    },
    created() {
        this.fetch_minions()
    },
    methods: {
        fetch_minions: function () {
            api.get("/list/minions")
                .then((response) => {
                    this.minions = response.data.minions;
                }).catch((error) => {
                    console.log(error)
                });
        }
    }
}
</script>

<style scoped></style>