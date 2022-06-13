class Staticmem{
     static s:number
      static disp():void{
        console.log("yo yo"+Staticmem.s)
     }
}
Staticmem.s=150
Staticmem.disp()