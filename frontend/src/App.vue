<template>
    <div class="center">
        <MinionComponent />
    </div>
</template>

<script>
import MinionComponent from "./components/minion/MinionComponent.vue";

export default {
    name: 'App',
    components: {
        MinionComponent
    }
}
</script>

<style>
:root {
    --yellow: #fce55b;
    --blue: #336188;

    /* --- MINION SIZES --- */

    /* SMALL */
    --small-width: 90px;
    --small-height: 170px;

    /* DEFAULT */
    --default-width: 100px;
    --default-height: 180px;
}

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}

.center {
    width: 100%;

    margin-left: 100px;
}

</style>
