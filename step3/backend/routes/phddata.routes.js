let mongoose = require('mongoose'),
    express = require('express'),
    router = express.Router();

let phddata = require('../models/phddata-schema');

router.route('/').get((req,res)=>{
    phddata.find((error,data)=>{
        if(error){
            return next(error)
        }else{
            res.json(data)
        }
    })
})


module.exports = router;