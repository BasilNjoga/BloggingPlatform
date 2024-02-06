import { reactive } from 'vue'


const store = reactive ({
    posts: [
        {
            id:0,
            title: "How to make your first blog",
            description: "This is easy, create a new account , click on create new blog, Add you blog details and save",
            date: new Date(),
        }, {
            id:1,
            title: "How to connect to an API",
            description: "use either axios or requests on javascript",
            date: new Date(),
        }, 
        {
            id:2,
            title: "How to connect to an API",
            description: "use either axios or requests on javascript",
            date: new Date(),
        },{
            id:3,
            title: "React or Vue ",
            description: "They have very similar features, learn javascript and choose one based on requirements",
            date: new Date(),
        },{
            id:4,
            title: "Sunflowers",
            description: 'Sunflowers are usually tall annual or perennial plants that in some species can grow to a height of 300 centimetres (120 inches) or more. Each "flower" is actually a disc made up of tiny flowers, to form a larger false flower to better attract pollinators. The plants bear one or more wide, terminal capitula (flower heads made up of many tiny flowers), with bright yellow ray florets (mini flowers inside a flower head) at the outside and yellow or maroon (also known as a brown/red) disc florets inside',
            date: new Date(),
        },{
            id:5,
            title: "lamborghini urus",
            description: "Lamborghini Urus is the first Super Sport Utility Vehicle in the world, merging the soul of a super sports car with the practical functionality of an SUV. Powered by Lamborghini’s 4.0-liter twin-turbo V8 engine, the Urus is all about a performance mindset that brings together fun-to-drive and astounding vehicle capabilities. The design, performance, driving dynamics and unbridled emotion flow effortlessly into this visionary realization of authentic Lamborghini DNA.",
            date: new Date(),
        },{
            id:6,
            title: "giraffe centre",
            description: "The Giraffe Centre is located in Lang'ata, approximately 20 kilometres from the centre of Nairobi, Kenya. It was established in order to protect the vulnerable giraffe, that is found only in the grasslands of East Africa.",
            date: new Date(),
        },
    ]
})

export default store