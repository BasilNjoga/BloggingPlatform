import axios from 'axios'

export default {
    data() {
        return {
            posts: []
        }
    },
    mounted() {
        axios.get('/blogapp/blogs')
        .then(response => this.posts = response.data)
    }
}