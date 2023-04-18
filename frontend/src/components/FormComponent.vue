<template>
    <form action="">
        <div>
            <label for="nome">Nome: </label>
            <input type="text" name="nome" id="nome-input">
        </div>

        <div>
            <label for="hair">Cabelo: </label>
            <select name="hair" id="hair">
                <option value="careca">Careca</option>
                <option value="em pé">Em pé</option>
                <option value="baixo">Baixo</option>
            </select>
        </div>

        <div>
            <label for="width">Width: </label>
            <select name="width" id="width-input">
                <option v-for="width in widths" :key="width.id" v-bind:value="width.id">
                    {{ width.name }}
                </option>
            </select>
        </div>

        <div>
            <label for="altura">Altura: </label>
            <select name="altura" id="altura">
                <option value="padrão">Padrão</option>
                <option value="baixo">Baixo</option>
                <option value="alto">Alto</option>
            </select>
        </div>

        <div>
            <label for="pose">Pose: </label>
            <select name="pose" id="pose">
                <option value="braço para cima">Braço para cima</option>
                <option value="Tpose">Tpose</option>
            </select>
        </div>
    </form>
</template>

<script>
//import axios from "axios";

export default {
    name: "FormComponent",
    data() {
        return {
            widths: []
        }
    },
    created() {
       console.log(this.get_widths())
    },
    methods: {
        get_widths: function() {
            fetch("http://127.0.0.1:5000/list/widths")
                .then(response => response.json())
                .then(json => {
                    return json
                })
        }
    }
}
</script>


<style></style>