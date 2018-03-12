var express  = require('express');
var session  = require('express-session');
var cookieParser = require('cookie-parser');
var mongoStore = require('connect-mongo')(session);
var app      = express();
var port     = process.env.PORT || 8080;
var mongoose = require('mongoose');
var passport = require('passport');
var flash    = require('connect-flash');
var path = require('path'),
    fs = require('fs');
 var http = require('http')
var server = http.createServer(app)


var configDB = require('./config/database.js');

mongoose.connect(configDB.url); 

require('./config/passport')(passport); 

app.configure(function() {

	app.use(express.cookieParser());
	app.use(express.bodyParser()); 
	app.use(express.static(path.join(__dirname, 'public')));
	app.set('views', __dirname + '/views');
	app.engine('html', require('ejs').renderFile);
	app.use(express.session({ 
	secret: 'knoldus', 
	resave: true,
	saveUninitialized: true,
	store: new mongoStore({
        mongooseConnection: mongoose.connection,
     	collection: 'sessions' // default
	})
	})); 
	app.use(express.bodyParser({uploadDir:'/images'}));
	app.use(passport.initialize());
	app.use(passport.session()); 
	app.use(flash()); 

});


require('./app/routes.js')(app, passport,server); 

/*
app.use(session({
  resave: true,
  saveUninitialized: true,
  secret: secret,
  store: new mongoStore({
    mongooseConnection: mongoose.connection,
    collection: 'sessions' // default
  })
}));
*/

server.listen(port);
console.log('Listening  to  port ' + port);


