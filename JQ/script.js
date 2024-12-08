$(document).ready(function () {
    $("#hoverDiv").hover(
        function () {
            // Change background color on mouse enter
            $(this).css("background-color", "yellow");
        },
        function () {
            // Reset background color on mouse leave
            $(this).css("background-color", "lightblue");
        }
    );
});
