$(".details").on("click", ".fa-pen", function() {
    $(this).replaceWith("<i class='fas fa-check'></i>");
    setTimeout(function() {
        $(".name").fadeOut();
        $(".email").fadeOut();
        $(".password").fadeOut();
        $(".interests").fadeOut();
    },100);
    $(".edit").fadeIn();
    $(".edit_last").fadeIn();
});

$(".details").on("click", ".fa-check", function (e) {
    $(this).replaceWith("<i class='fas fa-pen'></i>");
        setTimeout(function () {
            $(".name").fadeIn();
            $(".email").fadeIn();
            $('.interests').fadeIn();
         },100);
        $(".edit").fadeOut();
        $(".edit_last").fadeOut();

    e.stopPropagation();
});