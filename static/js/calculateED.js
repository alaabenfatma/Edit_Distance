var naiveReverse = function (string) {
    return string.split('').reverse().join('');
}
var longest = function(a,b){
    if(a.length>b.length)
        return a;
    else
        return b;
}
var removefrom = function(string,c){
    while(string.indexOf(c)!=-1)
        string = string.replace(c, '')
    return string;
}
$(document).ready(function () {
    $(document).on('click', '#calculate_ed', function () {
        var s1 = $('#s1').val();
        var s2 = $('#s2').val();
        $.getJSON('/calculate_ed', {
            s1: $('#s1').val(),
            s2: $('#s2').val()
        }, function (data) {
            let alignement = data.result[1];
            $("#results").remove();
            $("#deletions").remove();
            $('#ftwoStrings').append('<div id="results"></div>');
            $('#ftwoStrings').append('<div id="deletions"></div>');

            $('#results').append('<p> The edit distance is: ' + data.result[0] + '</p>');
            $('#results').append('<p> The alignment ref is: ' + alignement + '</p>');
            $('#deletions').append('<p> The deletions are going to be  : </p>');

            let j = 0;
            clean_alignement = removefrom(alignement,'-');
            while (j < clean_alignement.length ) {
                const element = clean_alignement[j];
                if (element == '.') {
                    $('#results').append('<span>' + s2[j] + '</span>');
                } else if (element == '/') {
                    $('#results').append('<span style="color:blue;font-weight:bold">' + s2[j] + '</span>');
                } else if (element == '+') {
                    $('#results').append('<span style="color:green;font-weight:bold">' + s2[j] + '</span>');
                }
                j++;
            }
            j = 0;
            while (j < alignement.length ) {
                const element = alignement[j];
                if (element == '-') {
                    $('#deletions').append('<p style="color:red;font-weight:red">(' + s1[j] + ', from :'+s1+', at : '+j+')</p>');
                }
                j++;
            }
           
        });
        return false;
    });
});