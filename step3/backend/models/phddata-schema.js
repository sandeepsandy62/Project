const mongoose = require('mongoose');
const Schema = mongoose.Schema;

let phddataSchema = new Schema({
    
    year:{
        type: Number
    },
    RUG:{
        type:Number
    },
    UvA:{
        type:Number
    },
    RU:{
        type:Number
    },
    VU:{
        type:Number
    },
    TUD:{
        type:Number
    },
    TUE:{
        type:Number
    },
    WUR:{
        type:Number
    },
    EUR:{
        type:Number
    },
    UU:{
        type:Number
    },
    LEI:{
        type:Number
    },
    UM:{
        type:Number
    },
    UT:{
        type:Number
    },
    UTi:{
        type:Number
    }

},{
    collection:'phddataset'
})

module.exports = mongoose.model('phddata',phddataSchema)