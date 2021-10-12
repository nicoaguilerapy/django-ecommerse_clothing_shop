function mycart() {
    $.ajax({
        url: "/cart/ajax/my-cart/",
        type: "GET",
        dataType: "json",
        success: function (response) {
            console.log(response)
        },
        error: function(response){

        }
    });
}

$(document).ready(function(){
    mycart();
});

// EndW