<script setup>
import Header from '../components/Header.vue'
import store from '../store.js'
import posts from '../blogsapi'

const getWordsNumber = (str) => (str.split(' ').length)

</script>

<template>
    <div class="Home">
        <main class="container mx-auto " >
            {{ posts }}
            <!-- <div class="PostItem border border-slate-700 mb-2 p-4 rounded-lg cursor-pointer"
             v-for="item, itemIndex in store.posts" :key="itemIndex"
             @click="$router.push(`/post/${item.id}`)">
            
            <h1 class="text-slate-900 text-3xl font-bold my-2"> 
                {{ item.title }}
            </h1>
            <p class="text-xl my-2"> {{ getWordsNumber(item.description)  }} words.</p> 
            </div> -->
        </main>
    </div>

</template>