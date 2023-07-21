const express  = require('express')
const mongoose = require('mongoose')
const cors = require('cors')
const SampleModel = require('./models/Sample')

const app = express()
app.use(cors());
app.use(express.json())

mongoose.connect("mongodb://localhost:27017/stock")
.then(()=>{
    console.log("connection successful")
})
.catch((err)=>{
    console.log(err);
});

app.get('/getSample', async (req,res)=>{
    try{
        const results = await SampleModel.find({})
        res.status(200).send(results);
    }
    catch(err){
        res.send(err)
    }
})


app.get('/getSample/name/:name', async (req,res)=>{
    try{
        const name = req.params.name;
        const result = await SampleModel.find({symbol:name},{tradeDate:1,open:1,high:1,low:1,close:1});
        res.send(result)
    }
    catch(err){
        res.send(err)
    }
}) 
app.get('/getSample/:tradeDate', async (req,res)=>{
    try{
        const name = req.params.tradeDate;
        const result = await SampleModel.find({tradeDate:name});
        res.send(result)
    }
    catch(err){
        res.send(err)
    }
})




app.listen(80,()=>{
    console.log("server is running")
})