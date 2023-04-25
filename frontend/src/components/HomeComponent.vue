<template>
    <HeaderComponent />
    <div class="wrapper">
        <div class="modal-container">
            <button id="btn-modal" class="btn" @click="toggle_modal">{{ btn_modal_txt }}</button>
            <Teleport to="#modal">
                <FormComponent v-if="modal_open" />
            </Teleport>
        </div>

        <!-- Listagem -->
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
            modal_open: false,
            btn_modal_txt: "Open Form"
        }
    },
    created() {

    },
    methods: {
        toggle_modal: function() {
            this.modal_open = !this.modal_open;
            this.btn_modal_txt = this.modal_open ? "Close Form" : "Open Form";
        }
    }
}
</script>

<style scoped>
.modal-container {
    width: 100%;
}

#btn-modal {
    width: 100px;
    height: auto;
    float: right;
    margin: 10px;
}

</style>