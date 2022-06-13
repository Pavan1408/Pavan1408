var Staticmem = /** @class */ (function () {
    function Staticmem() {
    }
    Staticmem.disp = function () {
        console.log("yo yo" + Staticmem.s);
    };
    return Staticmem;
}());
Staticmem.s = 150;
Staticmem.disp();
