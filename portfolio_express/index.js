const express = require('express')
const app = express()
const port = 3000

app.listen(port, () => {
    console.log(`express server open port : ${port} =>  http://localhost:3000`)
})

app.get('/user/:id', (req, res) => {
	const data = req.params
    res.send(data)
})

app.get('/user', (req, res) => {
	const data = req.query
    res.send(data)
})
