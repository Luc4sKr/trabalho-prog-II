<template>
    <HomeComponent />
</template>

<script>
import HomeComponent from './components/HomeComponent.vue';

export default {
    name: 'App',
    components: {
        HomeComponent
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;1,100;1,300;1,400;1,500;1,700;1,900&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

* {
    margin: 0px;
    padding: 0px;
    font-family: 'Montserrat', sans-serif;
}

body { 
    background-color: rgb(221, 247, 253);
}

.modal {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.btn {
    display: inline-block;
    border-radius: 7px;
    border: none;
    background: #1875FF;
    color: #fff;
    font-family: inherit;
    text-align: center;
    font-size: 12px;
    box-shadow: 0px 14px 56px -11px #1875FF;
    padding: 0.8em;
    transition: all 0.4s;
    cursor: pointer;
}
</style>
