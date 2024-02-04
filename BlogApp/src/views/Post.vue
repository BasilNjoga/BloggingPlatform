<script setup>
import { useRoute } from 'vue-router';
//import posts from '../views'
import store from '../store'

const route = useRoute()

const post = store.posts.find(x => x.id === parseInt(route.params.id))
</script>

<template>
    <div class="Post text-center conainer mx-auto">
        <h1 class="text-slate-900 text-4xl font-bold mb-4">{{ post.title }}</h1>
        <p class="text-md text-slate-400 my-2"> {{ post.date }} </p> 
        <p class="text-xl text-slate-500 my-2"> {{ post.description  }} words.</p>     

    </div>

</template>