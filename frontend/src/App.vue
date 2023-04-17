<template>
    <div class="center">
        <MinionComponent :key="minion.id" v-bind="minion" />
    </div>
</template>

<script>
import MinionComponent from "./components/minion/MinionComponent.vue";

export default {
    name: 'App',
    components: {
        MinionComponent
    },
    data() {
        return {
            minion: {
                id: 1,
                name: "Minion 1",
                hair: {
                    id: 1,
                    hair_name: "Algo"
                },
                width: {
                    id: 1,
                    minion_width: "default",
                    css_width_reference: "--small-width",
                    css_dungarees_reference: "--minion--dungarees-small" 
                }
            }
        }
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

    /* HIGH */
    --high-width: 120px;
    --high-height: 190px;

    /* DUNGAREES */
    --minion--dungarees-small: -5px;
    --minion--dungarees-default: -7px;
    --minion--dungarees-high: -11px;

    /* MINION */
    --minion-width: var(--default-width);
    --minion-height: var(--default-height);
    --minion-dungarees: var(--minion--dungarees-default);
}

.center {
    width: 300px;

    margin-left: 100px;
}

</style>
