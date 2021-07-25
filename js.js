function initScrollbar() {
    $(".blueScrollbar .v-scrollable").niceScroll({
        cursorcolor: "#0026BF",
        cursorborder: "1px solid #30BAFF", 
        autohidemode: false,
        cursorwidth: "10px"
    });
}

$(document).ready(function() {
    $(".v-scrollable").getNiceScroll().resize();

    $(".v-scrollable").mouseover(function() {
        $(".v-scrollable").getNiceScroll().resize();
    });
});