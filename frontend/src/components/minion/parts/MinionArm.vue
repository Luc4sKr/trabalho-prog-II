<template>
    <div class="arm">
        <div class="hand"></div>
    </div>
</template>

<script>
export default {
    name: "MinionArm",
    data() {
        return {

        }
    }
}
</script>

<style scoped>
.arm {
    background-color: var(--yellow);
    width: 10px;
    height: 30px;
    z-index: 30;

    position: absolute;
}

.hand {
    background-color: #000;
    width: 12px;
    height: 12px;
    border-radius: 50%;

    position: absolute;
    bottom: -5px;
    left: 50%;

    transform: translate(-50%, 0);
}
</style>