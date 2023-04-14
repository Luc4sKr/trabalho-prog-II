<template>
    <div class="dungarees-main">
        <div class="dungarees-front">
            <div class="left-strap"></div>
            <div class="right-strap"></div>
        </div>
        <div class="arms">
            
        </div>
    </div>
    <div class="legs">
        <div class="left-leg">
            <div class="left-foot"></div>
        </div>
        <div class="right-leg">
            <div class="right-foot"></div>
        </div>
    </div>
</template>

<script>

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
    width: 60px;
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
    top: -20px;
    left: -10px;
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
    top: -20px;
    right: -10px;
}

.legs {
    position: relative;
    top: 90%;
}

.left-leg,
.right-leg {
    background: #336188;
    height: 5px;
    width: 15px;
    z-index: 31;
}

.left-leg {
    position: absolute;
    left: 25%;
}

.right-leg {
    position: absolute;
    right: 25%;
}


.left-foot,
.right-foot {
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