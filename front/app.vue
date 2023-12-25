<script lang="ts" setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';

interface GetWishListDto {
    wish_list: string[];
}

const wishList = ref<string[]>([]);

async function getWishList(userId: number): Promise<string[]> {
    try {
        const res = await axios.get<GetWishListDto>(`http://0.0.0.0:8000/wish-list/${userId}`);
        return res.data.wish_list;
    } catch (err) {
        console.log(err);
        return [];
    }
}

onMounted(async () => {
    wishList.value = await getWishList(1);
});
</script>

<template>
    <div class="w-screen h-screen bg-neutral-500">
        <h1 class="text-center bg-indigo-500 text-white font-bold text-4xl p-4 mb-10">Wish list app</h1>
        <ul class="m-auto w-max flex flex-col gap-4 items-start justify-center">
            <li v-if="wishList.length" v-for="item in wishList" class="text-white text-xl text-left">
                {{ item }}
            </li>

            <h2 v-else class="text-gray-500">Empty list</h2>
        </ul>
    </div>
</template>
