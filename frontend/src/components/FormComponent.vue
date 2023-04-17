<template>
    <form action="">
        <div>
            <label for="nome">Nome: </label>
            <input type="text" name="nome" id="nome-input">
        </div>

        <div>
            <label for="hair">Cabelo: </label>
            <select name="hair" id="hair">
                <option value="careca">Careca</option>
                <option value="em pé">Em pé</option>
                <option value="baixo">Baixo</option>
            </select>
        </div>
        
        <div>
            <label for="largura">Largura: </label>
            <select name="largura" id="largura">
                <option value="médio">Médio</option>
                <option value="magro">Magrinho</option>
                <option value="gordo">Gordinho</option>
            </select>
        </div>

        <div>
            <label for="altura">Altura: </label>
            <select name="altura" id="altura">
                <option value="padrão">Padrão</option>
                <option value="baixo">Baixo</option>
                <option value="alto">Alto</option>
            </select>
        </div>

        <div>
            <label for="pose">Pose: </label>
            <select name="pose" id="pose">
                <option value="braço para cima">Braço para cima</option>
                <option value="Tpose">Tpose</option>
            </select>
        </div>
    </form>
</template>

<script>
export default {

}
</script>


<style>

</style>