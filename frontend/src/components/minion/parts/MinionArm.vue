<template>
    <div class="arm"
    v-bind-class="{ 'left-arm': left_arm, 'right-arm': !left_arm }">
        <div class="hand"
        v-bind:class="{ 'left-hand': left_arm, 'right-hand': !left_arm }"></div>
    </div>
</template>

<script>
export default {
    name: "MinionArm",
    data() {
        return {

        }
    },
    props: {
        left_arm: {
            type: Boolean,
            required: true
        }
    },
    created() {
        
    }
}
</script>

<style scoped>
.arm {
    background-color: var(--yellow);
    width: 10px;
    height: 35px;
    z-index: 30;
    position: absolute;

    border-radius: 100px;
}


.left-arm {
    transform: rotate(var(--minion-pose));
}

.right-arm {
    transform: rotate(calc(180deg - var(--minion-pose)));
}

.hand {
    background-color: #000;
    width: 12px;
    height: 12px;
    border-radius: 50%;

    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);
}

.left-hand {
    bottom: -5px;
}

.right-hand {
    top: -5px;
}
</style>