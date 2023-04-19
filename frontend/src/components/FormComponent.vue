<template>
    <div>
        <button @click="modal_open=true">Open</button>
    </div>
    <div class=".root">
        <div v-if="modal_open" class="modal">
            <form @submit.prevent="include_minion" id="minion-form">
                <div class="form-control">
                    <label for="nome">Nome: </label>
                    <input type="text" name="nome" id="nome-input" placeholder="Name" v-model="minion.name">
                </div>
                <div class="form-control">
                    <label for="hair">Hair Style: </label>
                    <select name="hair" id="hair" v-model="minion.hair_id">
                        <option v-for="hair in hairs" :key="hair.id" v-bind:value="hair.id">
                            {{ hair.hair_name }}
                        </option>
                    </select>
                </div>
                <div class="form-control">
                    <label for="width">Width: </label>
                    <select name="width" id="width-input" v-model="minion.width_id">
                        <option v-for="width in widths" :key="width.id" v-bind:value="width.id">
                            {{ width.width }}
                        </option>
                    </select>
                </div>
                <div class="form-control">
                    <label for="height">Height: </label>
                    <select name="height" id="height-input" v-model="minion.height_id">
                        <option v-for="height in heights" :key="height.id" v-bind:value="height.id">
                            {{ height.height }}
                        </option>
                    </select>
                </div>
                <div class="form-control">
                    <label for="pose">Pose: </label>
                    <select name="pose" id="pose" v-model="minion.pose_id">
                        <option v-for="pose in poses" :key="pose.id" v-bind:value="pose.id">
                            {{ pose.pose_name }}
                        </option>
                    </select>
                </div>
                <div class="buttons">
                    <button id="btn-close" class="btn" @click="modal_open = false">Close</button>
                    <button id="btn-register" class="btn">Register</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import api from "@/services/api.js";

export default {
    name: "FormComponent",
    data() {
        return {
            modal_open: true,

            widths: [],
            heights: [],
            hairs: [],
            poses: [],

            minion: {
                name: "",
                hair_id: 0,
                width_id: 0,
                height_id: 0,
                pose_id: 0
            }
        }
    },
    created() {
        this.fetch_widths();
        this.fetch_heights();
        this.fetch_hairs();
        this.fetch_poses();
    },
    methods: {
        fetch_widths: function () {
            api.get("/list/widths")
                .then((response) => {
                    this.widths = response.data.widths;
                }).catch((error) => {
                    console.log(error)
                });
        },
        fetch_heights: function () {
            api.get("/list/heights")
                .then((response) => {
                    this.heights = response.data.heights;
                }).catch((error) => {
                    console.log(error)
                });
        },
        fetch_hairs: function () {
            api.get("/list/hairs")
                .then((response) => {
                    this.hairs = response.data.hairs;
                }).catch((error) => {
                    console.log(error)
                });
        },
        fetch_poses: function () {
            api.get("/list/poses")
                .then((response) => {
                    this.poses = response.data.poses;
                }).catch((error) => {
                    console.log(error)
                });
        },

        include_minion: function() {
            api.post("/include/minion", this.minion)
                .then((response) => {
                    console.log(response)
                }).catch((error) => {
                    console.log(error)
                });
        }
    }
}
</script>

<style>
.root {
    position: relative;
}

.modal {
    width: 400px;
    height: 350px;
    box-shadow: 0px 0px 5px #000;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    background-color: var(--yellow);
}

#minion-form {
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: column;
    align-items: center;
}

.form-control {
    width: 200px;
    display: flex;
    flex-direction: column;
    margin: 10px;
}

.form-control > label {
    font-size: 14px;
}

.form-control > input, select {
    height: 20px;
}

.buttons {
    position: absolute;
    bottom: 10px;
}

.btn {
    width: 100px;
    margin: 5px;
}
</style>