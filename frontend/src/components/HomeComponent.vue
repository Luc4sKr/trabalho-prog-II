<template>
    <HeaderComponent />
    <div class="wrapper">
        <div class="modal-container">
            <button id="btn-modal" class="btn" @click="toggle_modal">Modal</button>
            <Teleport to="#modal">
                <FormComponent v-if="modal_open" />
            </Teleport>
        </div>
    </div>
</template>

<script>
import HeaderComponent from './HeaderComponent.vue';
import FormComponent from './FormComponent.vue';

export default {
    name: "HomeComponent",
    components: {
        HeaderComponent,
        FormComponent
    },
    data() {
        return {
            modal_open: true,
        }
    },
    created() {

    },
    methods: {
        toggle_modal: function() {
            this.modal_open = !this.modal_open;
        },
        close_modal: function() {
            this.modal_open = false;
        }
    }
}
</script>

<style scoped></style>