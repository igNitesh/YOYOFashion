






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
