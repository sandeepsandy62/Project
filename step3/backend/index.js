const express = require("express")
const mongoose = require("mongoose")
const cors = require("cors")
const bodyParser = require('body-parser');
const phddataRoute = require('../backend/routes/phddata.routes')

const password = "xxxxxxxxxx";
const dbname = "phddb";




mongoose
        .connect(
            `mongodb+srv://sandeepgogarla:${password}@cluster0.rozpydd.mongodb.net/${dbname}?retryWrites=true&w=majority`,
        )
        .then((x)=>{
            console.log(`Connected to Mongo! Database name : "${x.connections[0].name}"`)
        })
        .catch((err)=>{
            console.log('Error connecting to mongo',err.reason)
        })

const app = express()
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended:true
}));
app.use(cors());
app.use('/phddata',phddataRoute)

const port = process.env.PORT || 4000;

const server = app.listen(port, () => {
    console.log('Connected to port ' + port)
})

// Error Handling
app.use((req, res, next) => {
    next(createError(404));
});

app.use(function (err, req, res, next) {
    console.error(err.message);
    if (!err.statusCode) err.statusCode = 500;
    res.status(err.statusCode).send(err.message);
});


