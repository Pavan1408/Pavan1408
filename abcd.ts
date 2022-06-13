class Cars{
    carname : string;
    price : number;
    constructor(carname:string,price:number){
        this.carname=carname;
        this.price=price
    }
}


class Ds extends Car{
    disp():void{
        console.log(this.carname)
        console.log(this.price)
    }
}


class Hs extends D{
    di():void{
    console.log("hi")}
}


var a=new Hs("mercedes",500000)
a.di()
a.disp()