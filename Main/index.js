const express  = require('express')
const mongoose = require('mongoose')
const cors = require('cors')


const app = express()
app.use(cors());
app.use(express.json())

mongoose.connect("mongodb://localhost:27017/stack")
.then(()=>{
    console.log("connection successful")
})
.catch((err)=>{
    console.log(err)
});



app.listen(80,()=>{
    console.log("server is running")
})