<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';

const welcomeMessage = ref('');

onMounted(async () => {
    welcomeMessage.value = (await axios.get('http://0.0.0.0:8000/')).data.message;
});
</script>

<template>
    <h1>Wish list app</h1>
    <h2>{{ welcomeMessage }}</h2>
</template>
