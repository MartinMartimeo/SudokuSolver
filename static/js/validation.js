/**
 * User: Severin Orth <severin.orth@nicta.com.au>
 * Date: 12.03.13
 * Time: 16:38
 */

$(document).on('change', 'input[type=number]', function() {

    // Add error Classes
    $(this).parent().addClass("error");

    $(this).parent().removeClass("success");
    $(this).parent().removeClass("notice");

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

// Buttons
$(".btn-reset").on("click", function () {
    var sudoku = $("#sudoku");
    sudoku.find("input").parent().removeClass("success").removeClass("notice").removeClass("error").removeAttr("data-alert");
});

// Solve Button
$("#btn-solve").on("click", function () {

    var sudoku = $("#sudoku");

    $("#btn-solve").val("Solving").attr("disabled", "disable");
    $.getJSON('/solve', sudoku.find("input[type=number]"), function(data) {
        if (data.nsolvable) {
            alert("This Sudoku is not solvable!");
        } else {
            var result = data.result;

            $.each(result, function (coords, number) {
                var input = sudoku.find("input[name=x" + coords + "]");
                var num = input.val();
                if (num == number) {
                    input.parent().addClass("success");
                } else if (num) {
                    input.parent().addClass("notice");
                    input.val(number);
                } else {
                    input.val(number);
                }
            });

        }
    }).always(function () {
            $("#btn-solve").val("Solve").removeAttr("disabled");
    });
    return false;


});
// Solve Button
$("#btn-check").on("click", function () {

    var sudoku = $("#sudoku");

    $("#btn-check").val("Checking").attr("disabled", "disable");
    $.getJSON('/solve', sudoku.find("input[type=number]"), function(data) {
        if (data.nsolvable) {
            alert("This Sudoku is not solvable!");
        } else {
            alert("This Sudoku is solvable!");
        }
    }).always(function () {
            $("#btn-check").val("Check").removeAttr("disabled");
        });
    return false;


});