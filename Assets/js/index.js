
$(".sign").click(function(){
    $(".login").fadeToggle(300);
    setTimeout(function(){ 
        $(".signup").fadeToggle(300);
     }, 1000);
});
