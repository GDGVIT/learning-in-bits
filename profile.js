$(".details").on("click", ".fa-pen", function() {
    $(this).replaceWith("<i class='fas fa-check'></i>");
    setTimeout(function() {
        $(".name").fadeOut();
        $(".email").fadeOut();
        $(".password").fadeOut();
    },100);
    $(".edit").fadeIn();
});

$(".details").on("click", ".fa-check", function (e) {
    $(this).replaceWith("<i class='fas fa-pen'></i>");
        setTimeout(function () {
            $(".name").fadeIn();
            $(".email").fadeIn();
            $(".password").fadeIn();
         },100);
        $(".edit").fadeOut();

    e.stopPropagation();
});