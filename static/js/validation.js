/**
 * User: Severin Orth <severin.orth@nicta.com.au>
 * Date: 12.03.13
 * Time: 16:38
 */

$(document).on('change', 'input[type=number]', function() {

    // Add error Classes
    $(this).parent().addClass("error");

    if(!$(this).val()) {
        $(this).parent().removeClass("error");
        return;
    }

    var val = parseInt($(this).val());

    if ($(this).val() != val) {
        $(this).attr("data-alert", "Element contains nonnumeric characters");
        return;
    }

    if ($(this).attr("min")) {
        var min = parseInt($(this).attr("min"));
        if (val < min) {
            $(this).attr("data-alert", "Element is lower than it's boundary (>=" + min + ")");
            return
        }
    }
    if ($(this).attr("max")) {
        var max = parseInt($(this).attr("max"));
        if (val > max) {
            $(this).attr("data-alert", "Element is upper than it's boundary (<=" + max + ")");
            return
        }
    }

    // Everything was fine
    $(this).parent().removeClass("error");

});
$('input[type=number]').trigger('change');

// Apply tipsy
$('[data-alert]').tipsy({
    live: true,
    html: true,
    gravity: function() {
        if ($(this).offset().left < $(document).width() / 2) {
            return "w";
        } else {
            return "e";
        }
    },
    opacity: 0.9,
    title: function() {
        return $(this).attr("data-alert");
    }
});