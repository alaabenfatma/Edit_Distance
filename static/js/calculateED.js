$(document).ready ( function () {
    $(document).on('click','#calculate_ed',function () {
        var s1 = $('#s1').val();
	    var s2 = $('#s2').val();
	    $.getJSON('/calculate_ed', {
            s1: $('#s1').val(),
            s2: $('#s2').val()
          }, function(data) {
            $("#result").text(data.result);
          });
          return false;
        });
    });
