<template>
    <div class="body">
        <div class="head">
            <div class="eyes">
                <MinionGoggles />
            </div>
            <div class="lips"></div>
        </div>
        <div class="dungarees">
            <MinionDungarees />
        </div>
    </div>
</template>


<script>
import MinionGoggles from "./parts/MinionGoggles.vue";
import MinionDungarees from "./parts/MinionDungarees.vue";

export default {
    name: "MinionComponent",
    components: {
        MinionGoggles,
        MinionDungarees
    }
}
</script>


<style scoped>

.body {
    background-color: var(--yellow);
    width: var(--default-width);
    height: var(--default-height);
    position: relative;

    border-radius: 100px 100px 60px 60px;
}

.head {
    width: 100%;
    height: 100px;

    position: relative;
}

.eyes {
    width: 100%;
    height: 60px;
    position: relative;
}

.lips {
    background-color: var(--yellow);
    width: 35px;
    height: 15px;
    border-radius: 50%;
    border-bottom: 3px solid #000;

    /* centralizando */
    position: absolute;
    top: 80%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.dungarees {
    height: 80px;
}


</style>