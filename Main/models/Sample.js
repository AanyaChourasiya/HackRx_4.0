const mongoose = require("mongoose")

const SampleSchema = new mongoose.Schema({
    token: Number,
    exchid : Number,
    open : Number,
    high : Number,
    low : Number,
    close : Number,
    volume : Number,
    tradeDate : String,
    symbol : String
})

const SampleModel = mongoose.model("Sample","SampleSchema")
module.exports = SampleModel