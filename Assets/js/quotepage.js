
// $("input[type='text']").keypress(function(e){
//     if(e.which === 13){
//         var tag = $(this).val();
//         $(this).val("");
//         $("#two").append('<div class="col-4 col-sm-2"><div id="uno">'+tag+'<span><i class= "fa fa-times"></i></div></div></span>');

//     }
// });
$("#two").on("click", "span" , function(e){
    $(this).parent().addClass('hide').fadeOut(500,function(){
        // $(this).remove();
        $(this).parent().fadeOut();
    });
    e.stopPropagation();
});
