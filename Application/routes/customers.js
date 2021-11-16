var express = require('express');
var router = express.Router();
var customersMockData = require("../mockdata/customers")


router.route('/')
.get((req, res, next) => {
    res.send("working")
})

module.exports = router;
