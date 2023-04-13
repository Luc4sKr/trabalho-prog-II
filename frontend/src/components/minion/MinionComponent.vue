<template>
    <div class="body">
        <div class="head">
            <div class="eyes">
                <MinionGoggles />
            </div>
            <div class="lips"></div>
        </div>
    </div>
</template>


<script>
import MinionGoggles from "./parts/MinionGoggles.vue";

export default {
    name: "MinionComponent",
    components: {
        MinionGoggles
    }
}
</script>


<style scoped>
.body {
    background-color: var(--yellow);
    width: 100px;
    height: 180px;
    position: relative;

    border-radius: 100px 100px 60px 60px;
}

.head {
    width: 100%;
    height: 80px;

    position: relative;
}

.eyes {
    width: 100%;
    height: 60px;
    position: relative;
}

.lips {
    background-color: var(--yellow);
    width: 35px;
    height: 15px;
    border-radius: 50%;
    border-bottom: 3px solid #000;

    /* centralizando */
    position: absolute;
    top: 100%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.clothes {
    background-color: var(--blue);
    width: 100%;
    height: 70px;

    box-shadow: 2px 2px 4px -2px rgba(0, 0, 0, 0.5);

}

.arms {
    width: 100%;
    height: 10px;

    position: absolute;
    top: 15px;
}

.right-arm {
    background-color: var(--yellow);
    width: 10px;
    height: 60px;

    border-top-right-radius: 50%;

    position: absolute;
    left: 100%;
}

.legs {
    width: 100%;
    height: 30px;

    position: relative;
    top: 80%;
}

.left-leg {
    background-color: var(--blue);
    height: 100%;
    width: 20px;

    position: absolute;
    left: 20px;
}

.left-leg:after {
    content: "";
    background-color: #000;
    z-index: 11;
    width: 20px;
    height: 10px;

    position: absolute;
    left: 0px;
    top: 100%;
}

.right-leg {
    background-color: var(--blue);
    height: 100%;
    width: 20px;

    position: absolute;
    right: 20px;
}

.right-leg:after {
    content: "";
    background-color: #000;
    z-index: 11;
    width: 20px;
    height: 10px;

    position: absolute;
    left: 0px;
    top: 100%;
}
</style>