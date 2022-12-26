const express = require('express')
const app = express()
const port = 3000

app.get('/' ,function (req, res) {
	res.send('Hello World')
})

app.get('/test' ,function (req, res) {
    res.send('박정현 바보')
})

app.listen(port, () => {
    console.log(`express server open port : ${port} =>  http://localhost:3000`)
})