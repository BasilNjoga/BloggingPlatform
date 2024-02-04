<script >
import Header from '../components/Header.vue'
import store from '../store.js'
import axios from 'axios'
import { ref } from 'vue'


export default {

    setup () {

        const posts = ref('')

        axios.get('http://127.0.0.1:8000/blogapp/blogs')
            .then(response => {
                posts.value = response.data
            })

        return {
            posts
        }
    }
    
}
//const getWordsNumber = (str) => (str.split(' ').length)

</script>

<template>
    <div class="Home">
        <main class="container mx-auto " >
    
            <div class="PostItem border border-slate-700 mb-2 p-4 rounded-lg cursor-pointer"
            v-for="item, itemIndex in posts" :key="itemIndex"
            @click="$router.push(`/post/${item.id}`)">
                <h1 class="text-slate-900 text-3xl font-bold my-2"> {{  item.title  }}</h1>
                <p class="text-xl my-2"> {{ item.body }}</p>
            </div>
        </main>
    </div>

</template>