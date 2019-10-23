const express = require('express');
var bodyParser = require('body-parser');

const app = express();
const port = 5050;


app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));

app.listen(port, () => {
  console.info('Listening on %d', port);
});

app.get('/get', (req, res) => {
  res.render('get');
})

app.post('/post', (req, res) => {
  // console.log(req.body);
  res.render('data', {fname:req.body.fname,lname:req.body.lname,pass:req.body.pass});
});

