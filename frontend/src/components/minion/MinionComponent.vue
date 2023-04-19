<template>
    <div class="body">
        <div class="head">
            <MinionHair />
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
import MinionHair from "./parts/MinionHair.vue";

import { setPropertyStyleVal } from "@/scripts/utils.js";

export default {
    name: "MinionComponent",
    components: {
        MinionGoggles,
        MinionDungarees,
        MinionHair
    },
    data() {
        return {

        }
    },
    props: {
        name: {
            type: String,
            required: true
        },
        hair: {
            type: Object,
            required: true
        },
        width: {
            type: Object,
            required: true
        },
        height: {
            type: Object,
            required: true
        }
    },
    created() {
        setPropertyStyleVal("--minion-dungarees", this.width.css_dungarees_reference);
        setPropertyStyleVal("--minion-width", this.width.css_width_reference);
        setPropertyStyleVal("--minion-height", this.height.css_height_reference);
    }
}
</script>


<style scoped>
.body {
    background-color: var(--yellow);
    width: var(--minion-width);
    height: var(--minion-height);
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
    width: 100%;
    position: absolute;
    bottom: 0px;
}
</style>