function render(length){
    return Array(length).fill(" ").map((_, idx)=>  
    " ".repeat(length-idx-1)+"*"+Math.pow(Number("1".repeat(idx+1)), 2)+"*"+" ".repeat(length-idx-1).split()
    ).flat().forEach(_=>console.log(_));
}
render(4);
