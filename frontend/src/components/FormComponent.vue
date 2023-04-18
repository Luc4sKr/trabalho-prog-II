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
                <option value="em pé">Mohican</option>
                <option value="baixo">Baixo</option>
            </select>
        </div>

        <div>
            <label for="width">Width: </label>
            <select name="width" id="width-input">
                <option v-for="width in widths" :key="width.id" v-bind:value="width.id">
                    {{ width.width }}
                </option>
            </select>
        </div>

        <div>
            <label for="height">Height: </label>
            <select name="height" id="height-input">
                <option v-for="height in heights" :key="height.id" v-bind:value="height.id">
                    {{ height.height }}
                </option>
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
import api from "@/services/api.js";

export default {
    name: "FormComponent",
    data() {
        return {
            widths: [],
            heights: []
        }
    },
    created() {
        this.fetch_widths();
        this.fetch_heights();
    },
    methods: {
        fetch_widths: function() {
            api.get("/list/widths")
                .then((response) => {
                    this.widths = response.data.widths;
                }).catch((error) => {
                    console.log(error)
                });
        },
        fetch_heights: function() {
            api.get("/list/heights")
            .then((response) => {
                this.heights = response.data.heights;
            }).catch((error) => {
                console.log(error)
            })
        }
    }
}
</script>


<style></style>