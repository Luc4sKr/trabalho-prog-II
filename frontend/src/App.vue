<template>
    <HeaderComponent />

    <div>
        <FormComponent />
    </div>
</template>

<script>
import HeaderComponent from "./components/HeaderComponent.vue";
import FormComponent from "./components/FormComponent.vue";

//import MinionComponent from "./components/minion/MinionComponent.vue";

export default {
    name: 'App',
    components: {
        HeaderComponent,
        FormComponent
        
    },
    data() {
        return {
            minion: {
                id: 1,
                name: "Minion 1",

                hair: {
                    id: 1,
                    hair_name: "Default"
                },
                width: {
                    id: 1,
                    minion_width: "default",
                    css_width_reference: "--default-width",
                    css_dungarees_reference: "--minion--dungarees-default" 
                },
                height: {
                    id: 1,
                    minion_height: "default",
                    css_height_reference: "--default-height"
                }
            }
        }
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=DynaPuff:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Righteous&display=swap');

:root {
    /* COLORS */
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


    /* --- MINION --- */
    --minion-width: var(--default-width);
    --minion-height: var(--default-height);
    --minion-dungarees: var(--minion--dungarees-default);
}

* {
    margin: 0px;
    padding: 0px;
}

.center {
    width: 300px;

    margin-left: 100px;
}

</style>
