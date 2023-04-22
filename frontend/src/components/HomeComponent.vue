<template>
    <div class="form-container">
        <FormComponent />
    </div>
    <div class="list-container">
        <MinionListComponent />
    </div>
</template>

<script>
import FormComponent from './FormComponent.vue';
import MinionListComponent from './MinionListComponent.vue';

export default {
    name: "HomeComponent",
    components: {
        FormComponent,
        MinionListComponent
    },
    data() {
        return {

        }
    }
}
</script>

<style scoped>


</style>