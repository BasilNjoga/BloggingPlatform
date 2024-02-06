<script>
import axios from 'axios'


export default {

    data() {
        return {
       title: '',
       category: '',
       body: '',
       created_by: ''
   }
    },
    methods: { 
        createPost() {
            axios.post('https://blog-app-django-backend.onrender.com/blogapp/create',
            {
                title: this.title,
                category: this.category,
                body: this.body,
                created_by: this.created_by,
            }).then(response => {
                console.log(response)
            })
        }
    


},
}





</script>

<template>

    <main class=" container mx-auto">
        <h1 class="text-3xl font-bold mb-4">Create New Blog </h1>

        <form v-on:submit.prevent="createPost" class="place-items-center">
            <div class="place-items-center">
                <div class="mb-4">
                <lable class="text-xl" for="ftitle">Title</lable> <br>
                <input v-model="title" class="border-2 rounded-md border-slate-400 mt-2" type="text" id="ftitle"><br>
                </div>
             
                 <div class="mb-4">
                    <lable  class="text-xl" for="fcategory">Category</lable> <br>
                    <input v-model="category" class="border-2 rounded-md border-slate-400 mt-2" type="text" id="fcategory"> <br>
                 </div>

                 <div class="mb-4">
                <lable class="text-xl" for="fbody">Blog</lable> <br>
                <input v-model="body" class="border-2 p-10 rounded-md border-slate-400 mt-2" type="text" id="fbody"> <br>
                 </div>
                
                 <div class="mb-4">
                <lable class="text-xl" for="fcreator">Created By</lable> <br>
                <input v-model="created_by" class="border-2 rounded-md border-slate-400 mt-2" type="text" id="fcreator"> <br>
                 </div>
                
                
                <input class="p-4 font-bold bg-blue-300 rounded-lg" type="submit" value="Create Blog">
            </div>
        </form>
    </main>
</template>