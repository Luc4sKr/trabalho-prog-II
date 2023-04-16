<template>
    <div class="dungarees-main">
        <div class="dungarees-front">
            <div class="left-strap"></div>
            <div class="right-strap"></div>
        </div>
    </div>
    <div class="arms">
            <MinionArm class="left-arm"/>
            <MinionArm class="right-arm"/>
        </div>
    <div class="legs">
        <MinionLeg class="left-leg" :left_leg="true"/>
        <MinionLeg class="right-leg" :left_leg="false"/>
    </div>
</template>

<script>
import MinionLeg from "./MinionLeg.vue";
import MinionArm from "./MinionArm.vue";

export default {
    name: "MinionDungrees",
    components: {
        MinionLeg,
        MinionArm
    }
}
</script>

<style scoped>
.dungarees-main {
    background-color: var(--blue);
    width: 100%;
    height: 40px;
    border-bottom-left-radius: 25px;
    border-bottom-right-radius: 25px;

    position: absolute;
    bottom: 0;
}

.dungarees-front {
    background-color: var(--blue);
    width: 65%;
    height: 100%;
    border-radius: 10px 10px 0 0;

    position: relative;
    bottom: 20px;
    left: 50%;
    transform: translate(-50%, 0);
}

.left-strap {
    width: 6px;
    height: 40px;

    -webkit-transform: rotate(-50deg);
    transform: rotate(-50deg);
    background: #336188;
    border-radius: 16px 0 4px 4px;
    box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5);
    z-index: 50;

    position: absolute;
    bottom: 20px;
    left: var(--minion-dungares);
}

.right-strap {
    width: 6px;
    height: 40px;
    
    -webkit-transform: rotate(50deg);
    transform: rotate(50deg);
    background: #336188;
    border-radius: 0 16px 4px 4px;
    box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5);
    z-index: 50;

    position: absolute;
    bottom: 20px;
    right: var(--minion-dungares);
}

.arms {
    position: relative;
    top: -5px;
    transform: rotate(90deg);
}

.left-arm {
    top: calc(var(--minion-width) / 2 - 1px);
}

.right-arm {
    bottom: calc(var(--minion-width) / 2 - 1px);
    transform: rotate(180deg);
}

.legs {
    position: relative;
    top: 90%;
}

.left-leg {
    position: absolute;
    left: 25%;
}

.right-leg {
    position: absolute;
    right: 25%;
}
</style>