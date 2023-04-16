<template>
    <div class="goggles">
        <div class="frame">
            <div class="lense">
                <div class="eye-ball">
                    <div class="eye-pupil"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "MinionGoggles"
}
</script>

<style scoped>
.goggles {
    width: 100%;
    height: 15px;
    background: #2a2a2a;
    border-radius: 2px;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    z-index: 2;

    position: relative;
    top: 70%;
}

.frame {
    background: #898989;
    border-radius: 2px;
    box-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    height: 100%;
    width: 50px;
    z-index: 11;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.lense {
    width: 35px;
    height: 35px;
    background: #000;

    border-radius: 50%;
    border: solid 5px #898989;
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
    z-index: 12;

    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.eye-ball {
    width: 100%;
    height: 100%;
    background: #ffffff;
    border-radius: 50%;
    box-shadow: 1px 1px 14px rgba(0, 0, 0, 0.5) inset;
    z-index: 14;
    position: relative;
}

.eye-pupil {
    width: 5px;
    height: 5px;
    background: #000000;
    border-radius: 50%;
    border: solid 5px #3F1515;
    z-index: 14;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>