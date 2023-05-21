// var x = document.getElementById('quantity');
// var productid = document.getElementById('product');

// // var csrf = document.getElementById('csrf')
// // function sendcsrf()
// // {
// //     csrf_token = csrf.value
// //     console.log(csrf_token)
// // }
// function increaseQuantatiy(){
//     console.log("clicked")
//     x.value = +x.value + +1
//     console.log(x.value)
// }
// function decreaseQuantatiy(){
//     console.log("clicked")
//     if(x.value>1)
//     {
//         x.value = +x.value - +1
//     }
//     else{
//         x.value = '1'
//     }
//     console.log(x.value)
// }






//  function addtocart()
//  {
//     console.log('add to cart')
//     Quantity = x.value
//     const xhr = new XMLHttpRequest();
//     xhr.open('POST', '/shop_details' , true)
//     xhr.setRequestHeader('Content-type' , 'application/x-www-form-urlencoded')
//     xhr.setRequestHeader('X-CSRFToken' , csrf.value)
//     data = `quantity=${Quantity}&product=${productid.value}`
//     xhr.send(data);

//     xhr.onload = function() {
//         console.log(this.status)
//         if(this.status !== 200){
            
//             alert("something went wrong")
            
//         }
//         else{
//             console.log("done")
//             window.location.reload()
//         }
//     }
// }









document.addEventListener('DOMContentLoaded', function() {
    const decreaseBtn = document.getElementById('decrease-quantity');
    const increaseBtn = document.getElementById('increase-quantity');

    decreaseBtn.addEventListener('click', function() {
        const quantityInput = document.getElementById('quantity');
        let quantity = parseInt(quantityInput.value);
        if (quantity > 1) {
            quantity -= 1;
            quantityInput.value = quantity.toString();
        }
    });

    increaseBtn.addEventListener('click', function() {
        const quantityInput = document.getElementById('quantity');
        let quantity = parseInt(quantityInput.value);
        quantity += 1;
        quantityInput.value = quantity.toString();
    });
});
