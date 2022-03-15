pm.test("Status code = 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response time < 100ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(100);
});

pm.test("Response body size < 500 B", function () {
    pm.expect(pm.response.responseSize).to.be.below(500);
});

pm.test("Check if the array is not empty", () => {
  pm.expect(pm.response.json().errors).not.to.be.null;
});

pm.test("Check the response data type", () => {
  pm.expect(pm.response.json()).to.be.an("object");
  pm.expect(pm.response.json().exchanges).to.be.a("array");
});
