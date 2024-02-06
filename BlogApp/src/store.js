import { reactive } from 'vue'


const store = reactive ({
    posts: [
        {
            id:1,
            title: "How to make your first blog",
            description: "This is easy, create a new account , click on create new blog, Add you blog details and save",
            date: new Date(),
        }, {
            id:2,
            title: "How to connect to an API",
            description: "use either axios or requests on javascript",
            date: new Date(),
        }, {
            id:3,
            title: "React or Vue ",
            description: "They have very similar features, learn javascript and choose one based on requirements",
            date: new Date(),
        },
    
    ]
})

export default store