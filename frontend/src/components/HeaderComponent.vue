<template>
    <header>
        <h1>MINIONS GENERATOR</h1>
    </header>
</template>

<script>
export default {
    name: "HeaderComponent",
    data() {
        return {

        }
    }
}
</script>

<style>
header {
    font-family: 'Righteous', cursive;
    background-color: var(--yellow);
    height: 150px;

    display: flex;
    justify-content: center;
    align-items: center;
    
}

h1 {
    text-align: center;
    font-size: 75px;
}
</style>