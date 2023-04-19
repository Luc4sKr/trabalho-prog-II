<template>
    <div class="form-container">
        <FormComponent />
    </div>
    <div class="list-container">

    </div>
</template>

<script>
import FormComponent from './FormComponent.vue';

export default {
    name: "HomeComponent",
    components: {
        FormComponent
    },
    data() {
        return {

        }
    }
}
</script>

<style>

</style>