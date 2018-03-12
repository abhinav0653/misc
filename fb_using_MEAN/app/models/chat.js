var mongoose = require('mongoose');
var bcrypt   = require('bcrypt-nodejs');

var chatSchema = mongoose.Schema({
    chat             : {
	data           :String,
     }
});



module.exports = mongoose.model('chat',chatSchema);
