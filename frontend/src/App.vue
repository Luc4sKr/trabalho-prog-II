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

* {
    margin: 0px;
    padding: 0px;
    font-family: 'Roboto', sans-serif;
}

.modal {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>
