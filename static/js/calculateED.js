var naiveReverse = function (string) {
    return string.split('').reverse().join('');
}
$(document).ready(function () {
    $(document).on('click', '#calculate_ed', function () {
        var s1 = $('#s1').val();
        var s2 = $('#s2').val();
        $.getJSON('/calculate_ed', {
            s1: $('#s1').val(),
            s2: $('#s2').val()
        }, function (data) {
            alignement = data.result[1];
            //alignement = naiveReverse(alignement);
            $("#results").remove();
            $("#deleted").remove();
            $('#ftwoStrings').append('<div id="results"></div>');
            $('#results').append('<p> The edit distance is: ' + data.result[0] + '</p>');
            $('#results').append('<p> The alignment ref is: ' + alignement + '</p>');

            let j = 0;
            tempo_alignement = alignement.replace('-', '')
            while (j < alignement.length ) {
                const element = alignement[j];
                if (element == '.') {
                    $('#results').append('<span>' + s2[j] + '</span>');
                } else if (element == '/') {
                    $('#results').append('<span style="color:blue;font-weight:bold">' + s2[j] + '</span>');
                } else if (element == '+') {
                    $('#results').append('<span style="color:green;font-weight:bold">' + s2[j] + '</span>');
                } else if (element == '-') {
                    $('#results').append('<span style="color:red;font-weight:bold">_</span>');
                    alignement = alignement.slice(0, j-1) + alignement.slice(j);
                    continue;
                }
                j++;
            }
           
        });
        return false;
    });
});