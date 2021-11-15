const request = require('supertest');
const app = require('../../Application/app');
//const screen = require('@testing-library/jest-dom');



describe('CUSTOMERS', () => {

    describe('GET method for CUSTOMER endpoint', () => {

        //------------TEST FOR ALL CUSTOMERS---------------------------------+

        test("respond with a 200 status code", async () => {
            const response = await request(app).get("/api/customers")
            expect(response.statusCode).toBe(200)
        })

        test("the response must be an array of customers", async () => {
            const response = await request(app).get("/api/customers")
            expect(Array.isArray(response.body.customers) == true).toBe(true)
        })
        test("the response must have at least one customer", async () => {
            const response = await request(app).get("/api/customers")
            expect(response.body.customers).not.toHaveLength(0)
        })

        //for the homepagr - check that the front page is uploaded
        test("check that it returns the homepage", async () => {
            const response = await request(app).get("/")
            //expect(response).toBe('text/html; charset=utf-8')
            expect(response.header["content-type"]).toBe('text/html; charset=utf-8')
        })
        //check for content of the received file
        test('checks that the html contains TJX Capstone', async ()=>{
            const response = await request(app).get("/")
            expect(response.text.includes("TJX Capstone API")).toBe(true)

        })
        






    })
})