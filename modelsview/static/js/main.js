let totalCost=document.querySelector('.total-cost')
let quantity=document.querySelector('.quantity')
let rate=document.querySelector('.rate')
let saveBtn=document.querySelector('.save-item-btn')
let goBack=document.querySelector('.go-back')
let viewBtn=document.querySelector('.view-items')

let total=0

let setTotalCost=()=>{
    total=quantity.value * rate.value
    totalCost.value=total
    console.log(typeof total)
    if(Number.isNaN(total)){
        console.log("kk")
        saveBtn.setAttribute('disabled',true)
    }
    else{
        console.log("kk-btn")

        saveBtn.removeAttribute('disabled')
    }
}

let goHome=()=>{
    window.history.go(-1)
}

let viewTable=()=>{
    window.location.href='/list-view/'
}

quantity.addEventListener('input',setTotalCost)
quantity.addEventListener('change',setTotalCost)
rate.addEventListener('input',setTotalCost)
rate.addEventListener('change',setTotalCost)
goBack.addEventListener('click',goHome)
viewBtn.addEventListener('click',viewTable)
