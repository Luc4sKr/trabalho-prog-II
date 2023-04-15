<template>
    <div class="leg">
        <div class="foot"
        v-bind:class="{ 'left-foot': left_leg, 'right-foot': !left_leg }"></div>
    </div>
</template>


<script>
export default {
    name: "MinionLeg",
    data() {
        return {
            
        }
    },
    props: {
        left_leg: {
            type: Boolean,
            required: false,
            default: true
        }
    }
}
</script>

<style scoped>
.leg {
    background: #336188;
    height: 5px;
    width: 15px;
    z-index: 31;
}

.foot {
    width: 20px;
    height: 5px;
    background: #272727;
    border-bottom: 2px solid #000000;
    box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    z-index: 34;

    position: absolute;
    top: 100%;
}

.left-foot {
    border-radius: 10px 0 4px 4px;
    left: -5px;
}

.right-foot {
    border-radius: 0 10px 4px 4px;
    right: -5px;
}
</style>