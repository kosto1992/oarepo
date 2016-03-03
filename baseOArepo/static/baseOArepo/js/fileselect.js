/**
 * Created by simeki on 3.3.16., taken from http://www.abeautifulsite.net/whipping-file-inputs-into-shape-with-bootstrap-3/
 */

$(document).on('change', '.btn-file :file', function() {
    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);
});

$(document).ready( function() {
    $('.btn-file :file').on('fileselect', function(event, numFiles, label) {
        $(event.currentTarget).parents('.input-group').find('.file-notify').val(label);
    });
});