<script >
import axios from 'axios'


// Function to call the Available Django API
export default {

        data() {
            return {
                posts: [],
                showNextButton: false,
                showPreviousButton: false,
                currentPage: 1
        
            }
        },
        mounted() {
            this.getPosts();
        },
        methods: { 
            getPosts() {
                this.showNextButton = false
                this.showPreviousButton = false
                axios.get(`https://blog-app-django-backend.onrender.com/blogapp/blogs?page=${this.currentPage}`)
                    .then(response => {
                        
                        this.formatPosts(response.data.results)
                        console.log(response.data.results)
                        if (response.data.next) {
                            this.showNextButton = true
                        }

                        if (response.data.previous) {
                            this.showPreviousButton = true
                        }
                })
            },
            formatPosts(posts) {
                for (let key in posts) {
                    this.posts.push({ ...posts[key], id: key })
                }
            },
            goToNextPage() {
                this.currentPage += 1
                this.getPosts()
                
            },
            goToPreviousPage() {
                this.currentPage -= 1
                this.getPosts()
            }



        },
}


//const getWordsNumber = (str) => (str.split(' ').length)

</script>
<style>
.row {
    display: flex;
}
.column {
    flex: 50%;
}

</style>

<template>
    <div class="Home">

        <main class=" mx-auto " >
            <button @click="$router.push('/create')" class="p-4 font-bold bg-blue-100 rounded-lg createbutton ml-20 mb-5"> Create New Blog </button>
            <div class="grid grid-cols-2">
            <div class="ml-4 PostItem border border-slate-700 mb-4 p-4 rounded-lg cursor-pointer"
            v-for="item, itemIndex in posts" :key="itemIndex"
            @click="$router.push(`/post/${item.id}`)">
                <h1 class="text-slate-900 text-3xl font-bold my-2"> {{  item.title  }}</h1>
                <p class="text-xl my-2"> {{ item.body }}</p>
            </div>
            </div>

            <div class="button">
                <button @click="goToPreviousPage()" class="p-2 font-bold bg-blue-100 rounded-lg createbutton ml-20 mb-5" v-if="showPreviousButton">Previous</button>
                <button @click="goToNextPage()" class="p-2 font-bold bg-blue-100 rounded-lg createbutton ml-20 mb-5" v-if="showNextButton">Next</button>
                
            </div>

        </main>
    </div>

</template>